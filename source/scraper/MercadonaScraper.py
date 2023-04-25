from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
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

        # Obtener el User-Agent utilizando JavaScript  
        user_agent = self.driver.execute_script("return navigator.userAgent") 
        print('El User-Agent es:', user_agent)  

        self.driver.get(self.url)
        self.wait_for_page_to_load()

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

        self.wait_for_page_to_load()

    def navigate_to_next_categories(self)-> bool:
        
        next_subcategories = self.driver.find_elements(By.XPATH, '//button[contains(@class, "next-subcategory")]')

        if(next_subcategories == None 
           or len(next_subcategories) == 0):
            return False

        next_subcategories[0].click()
        self.wait_for_page_to_load()

        return True

    def get_all_groups_categories(self):
        return self.driver.find_elements(By.XPATH, '//li[contains(@class, "category-menu__item")]')
    
    def navigate_to_next_group_categories(self, category_group):

        button = category_group.find_element(By.TAG_NAME, 'button')
        button.click()
        self.wait_for_page_to_load()
        
    def get_all_product_page(self):

        time.sleep(1)

        products:list[Product] = []
        set_products_button = self.driver.find_elements(By.XPATH, '//button[@data-test="open-product-detail"]')

        for button in set_products_button:
            try:
                products.append(self.get_product(button))
            except NoSuchElementException:
                time.sleep(5)
                continue

        return products

    def get_product(self, buttom:WebElement) -> Product:

        buttom.click()
        time.sleep(1)

        group_name = ""
        group_name_elements = self.driver.find_elements(By.XPATH, '//span[@class="subhead1-r"]')

        if group_name_elements and len(group_name_elements) > 0:
            group_name = group_name_elements[0].text

        group_category = ""
        group_name_categories = self.driver.find_elements(By.XPATH, '//span[@class="subhead1-sb"]')
        
        if group_name_categories and len(group_name_categories) > 0:
            group_category = group_name_categories[0].text
        
        product_name = self.driver.find_element(By.XPATH, '//h1[@class="title2-r private-product-detail__description" and @tabindex="0"]').text
        price_web_elements = self.driver.find_elements(By.XPATH, '//p[@class="product-price__unit-price large-b"]')

        if price_web_elements and len(price_web_elements) > 0:
            product_price = price_web_elements[0].text
        else:
            product_price = self.driver.find_element(By.XPATH, '//p[@class="product-price__unit-price large-b product-price__unit-price--discount"]').text

        product_amount = self.driver.find_element(By.XPATH, '//p[@class="product-price__extra-price title1-r"]').text

        div_product_information_text = self.driver.find_element(By.XPATH, '//div[@class="product-format product-format__size" and @tabindex="0"]').text.split('|')

        product_unit = div_product_information_text[0]
        product_price_by_unit = div_product_information_text[1]

        close_product_button = self.driver.find_element(By.XPATH, '//button[@data-test="modal-close-button"]')
        close_product_button.click()

        return Product(
            group_name, 
            group_category, 
            product_name, 
            product_price,
            product_amount,
            product_unit,
            product_price_by_unit)

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def close_the_browser(self):
        self.driver.quit()
    