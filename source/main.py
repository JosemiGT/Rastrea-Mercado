
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
    
    try:
        mercadona_scraper.complete_postal_code()
        mercadona_scraper.accept_cookies()
        time.sleep(2)
        mercadona_scraper.navigate_to_categories()

        products = mercadona_scraper.get_all_product_page()
        product_repository.save_products(products)
        mercadona_scraper.close_the_browser()
        
    except:
        # mercadona_scraper.close_the_browser()
        raise
