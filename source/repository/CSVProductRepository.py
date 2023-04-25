import csv
from models.product import Product

class CSVProductRepository:
    def __init__(self, filename):  
        self.filename = filename  

    def insert_headers(self):

         with open(self.filename, 'w', newline='', encoding='utf8') as csv_file:

            field_names = ['Grupo', 
                           'Categoria', 
                           'Nombre', 
                           'Precio', 
                           'Cantidad', 
                           'unidad-medida', 
                           'Precio-und-medida']
            
            csv_writer = csv.DictWriter(
            csv_file, 
            delimiter=',',
            fieldnames=field_names,
            quotechar='"', 
            quoting=csv.QUOTE_MINIMAL)
            
            csv_writer.writeheader() 

    def save_products(self, products:list[Product]):

        with open(self.filename, mode='a', newline='', encoding='utf8') as csv_file:

            writer = csv.writer(csv_file)  

            for product in products:  
                writer.writerow([
                    product.group_name, 
                    product.category_name, 
                    product.product_name, 
                    product.product_price, 
                    product.product_amount, 
                    product.product_unit, 
                    product.product_price_by_unit])  