from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from class_product import Product                    
import logging
from graficar_productos import ProductGraph
from urls import falabella
from urls import ripley
from excel_exporter import ExcelExporter
class IphonesScraper:
    def __init__(self):
        self.products = []
        self.logger = logging.getLogger(__name__)

    def falabella(self, url):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(url)
            wait = WebDriverWait(self.driver, 5)
            boxs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jsx-200723616')))
            
            if boxs:
                count = 0
                for box in boxs:
                    count + 1
                    elements = box.find_elements(By.CLASS_NAME, 'jsx-2889528833')
                    producto = []
                    for element in elements:
                        text = element.text
                        if "iPhone" in text:
                            producto.append(text)
                        if "$" in text:
                            producto.append(text)
                    if len(producto) > 2:
                        product_instance = Product(producto[0], producto[1])
                        self.products.append(product_instance)
                self.logger.info("completed")
            else:
                self.logger.warning("No elements found.")
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
        finally:
            self.driver.quit()
    def ripley(self, url):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(url)
            wait = WebDriverWait(self.driver, 5)
            boxs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'catalog-product-item')))
            if boxs:
                for box in boxs:
                    name = box.find_elements(By.CLASS_NAME, 'catalog-product-details__name')
                    price = box.find_elements(By.CLASS_NAME, 'catalog-prices__card-price')
                    if name and price:
                        product_instance = Product(name[0].text, price[0].text)
                        self.products.append(product_instance)
                self.logger.info("completed")
            else:
                self.logger.warning("No elements found.")
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
        finally:
            self.driver.quit()
    def get_products(self):
        for product in self.products:
            print(product.get_info())
    
    def plot_products(self):
        try:
            if not self.products:
                self.logger.warning("No products to plot.")
                return
            
            product_graph = ProductGraph(self.products)
            product_graph.plot_prices()
        except Exception as e:
            self.logger.error(f"An error occurred while plotting products: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scraper = IphonesScraper()
    for url in falabella:
        scraper.falabella(url)
    for url in ripley:   
        scraper.ripley(url)
    print(len(scraper.products))
    excel_exporter = ExcelExporter(scraper.products)
    excel_exporter.export_to_excel("products.xlsx")