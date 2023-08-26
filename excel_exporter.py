from openpyxl import Workbook

class ExcelExporter:
    def __init__(self, products):
        self.products = products

    def export_to_excel(self, filename):
        workbook = Workbook()
        sheet = workbook.active

        sheet.append(['Product', 'Price'])  # Headers

        for product in self.products:
            sheet.append(product.get_info())

        workbook.save(filename)