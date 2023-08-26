class Product:
    def __init__(self, product: str, price: float):
        self.product = product
        self.price = price
    def get_info(self):
        return (self.product, self.price)