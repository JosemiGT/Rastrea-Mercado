
class Producto:  
    def __init__(self, 
                 category_id:int, 
                 category_name:str, 
                 product_id:int,  
                 product_name:str, 
                 product_brand, 
                 product_origin, 
                 product_pvp,  
                 product_amount, 
                 product_unit, 
                 product_price, 
                 product_description,  
                 product_picture):
        self.category_id = category_id  
        self.category_name = category_name  
        self.product_id = product_id  
        self.product_name = product_name  
        self.product_brand = product_brand  
        self.product_origin = product_origin  
        self.product_pvp = product_pvp  
        self.product_amount = product_amount  
        self.product_unit = product_unit  
        self.product_price = product_price  
        self.product_description = product_description  
        self.product_picture = product_picture  
