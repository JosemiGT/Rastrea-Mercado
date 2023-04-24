from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.common.keys import Keys
import time
from models.Product import Product

class MercadonaScraper():

    def __init__(self, postal_code:int):
        self.url:str = "https://tienda.mercadona.es/"
        self.postal_code:int = postal_code
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def complete_postal_code(self):

        postal_code_box = self.driver.find_element(By.NAME, 'postalCode')
        postal_code_box.send_keys(str(self.postal_code))

        postal_code_buttom = self.driver.find_element(By.XPATH, '//button[@data-test="postal-code-checker-button"]')
        postal_code_buttom.click()

        time.sleep(1)

    def accept_cookies(self):
        cookies_buttom = self.driver.find_element(By.XPATH, '//button[contains(text(), "Aceptar todas")]')
        cookies_buttom.click()

        time.sleep(1)

    def navigate_to_categories(self):
        
        categories_section = self.driver.find_element(By.XPATH, '//a[@href="/categories"]')
        categories_section.click()

        titulo = self.driver.title  
        print('El título de la página es:', titulo)
        time.sleep(1)

    def get_all_product_page(self):

        products:list[Product] = []
        set_products_button = self.driver.find_elements(By.XPATH, '//button[@data-test="open-product-detail"]')

        for button in set_products_button:
            products.append(
                self.get_product(button))
            
        return products

    def get_product(self, buttom:WebElement) -> Product:

        buttom.click()

        group_name = self.driver.find_element(By.XPATH, '//span[@class="subhead1-r"]').text
        group_category = self.driver.find_element(By.XPATH, '//span[@class="subhead1-sb"]').text
        product_name = self.driver.find_element(By.XPATH, '//h1[@class="title2-r private-product-detail__description" and @tabindex="0"]').text
        product_unit_price = self.driver.find_element(By.XPATH, '//p[@data-test="product-price"]').text

        close_product_button = self.driver.find_element(By.XPATH, '//button[@data-test="modal-close-button"]')
        close_product_button.click()

        return Product(
            group_name, 
            group_category, 
            product_name, 
            product_unit_price)

    def close_the_browser(self):
        self.driver.quit()
    