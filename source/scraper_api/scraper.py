#!/usr/bin/env python  

from datetime import datetime  
from scraper_aux import get_api_categories
from scraper_aux import api_product_data_extractor_by_category
from scraper_aux import save_product_data_to_csv

MERCADONA_TIENDA_URL_API_PRODUCTS = "https://tienda.mercadona.es/api/products/"
MERCADONA_TIENDA_URL_API_CATEGORIES = "https://tienda.mercadona.es/api/categories/"
MERCADO_URL_OPTIONS = "/?lang=es&wh=bcn1"
OUTPUT_FILE = "datos_mercadona.csv"
DELAY_TIME = 5

if __name__ == "__main__":

    today = datetime.today() 
    date_string = today.strftime('%Y%m%d')  

    api_categories_list = get_api_categories(
        MERCADONA_TIENDA_URL_API_CATEGORIES + MERCADO_URL_OPTIONS)

    product_collection = api_product_data_extractor_by_category(
        MERCADONA_TIENDA_URL_API_CATEGORIES, 
        MERCADONA_TIENDA_URL_API_PRODUCTS, 
        MERCADO_URL_OPTIONS, 
        DELAY_TIME, 
        api_categories_list)

    save_product_data_to_csv(
        product_collection,
        date_string + "_" + OUTPUT_FILE)