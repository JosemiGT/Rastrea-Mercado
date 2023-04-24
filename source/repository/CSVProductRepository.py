import csv
from models.Product import Product

class CSVProductRepository:
    def __init__(self, filename):  
        self.filename = filename  
          
    def save_products(self, products:list[Product]):

        with open(self.filename, mode='w', newline='') as csv_file:
              
            writer = csv.writer(csv_file)  
            writer.writerow(['Grupo', 'Categoría', 'Nombre', 'Precio'])

            for product in products:  
                writer.writerow([product.group_name, product.category_name, product.product_name, product.product_price])  