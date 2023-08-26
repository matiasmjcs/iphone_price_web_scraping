import matplotlib.pyplot as plt

class ProductGraph:
    def __init__(self, products):
        self.products = products
        
    def plot_prices(self):
        product_names = [product.product for product in self.products]
        prices = [product.price for product in self.products]
        prices_before = [product.price_before for product in self.products]
        
        x = range(len(product_names))
        
        plt.figure(figsize=(10, 6))
        plt.bar(x, prices, width=0.4, align='center', label='Price')
        plt.bar([pos + 0.4 for pos in x], prices_before, width=0.4, align='center', label='Price Before')
        
        plt.xlabel('Products')
        plt.ylabel('Price')
        plt.title('Product Prices Comparison')
        plt.xticks(x, product_names, rotation='vertical')
        plt.legend()
        
        plt.tight_layout()
        plt.show()
