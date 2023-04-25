
from scraper.MercadonaScraper import MercadonaScraper
from repository.CSVProductRepository import CSVProductRepository
import time
from datetime import datetime  

OUTPUT_FILE = "datos_mercadona.csv"

if __name__ == "__main__":

    print("Iniciando Mercadona Scraper")

    today = datetime.today() 
    date_string = today.strftime('%Y%m%d')  
    mercadona_scraper = MercadonaScraper(46001)
    product_repository = CSVProductRepository(
        date_string + "_" + OUTPUT_FILE)
    
    product_repository.insert_headers()
    mercadona_scraper.complete_postal_code()
    mercadona_scraper.accept_cookies()
    time.sleep(2)
    mercadona_scraper.navigate_to_categories()

    categories_groups = mercadona_scraper.get_all_groups_categories()

    there_are_next_category = True
    there_are_next_group = True

    for group in categories_groups:
        
        mercadona_scraper.navigate_to_next_group_categories(group)

        while(there_are_next_category):
            product_repository.save_products(mercadona_scraper.get_all_product_page())
            there_are_next_category = mercadona_scraper.navigate_to_next_categories()

        there_are_next_category = True

    mercadona_scraper.close_the_browser()
