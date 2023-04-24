import requests
import json
import csv
import time

def get_api_categories(url) -> list[int]:
  """ Get all category IDs available in the mercadona API.
  Args:
      url (str): API Category Mercadona URL.

  Raises:
      requests.exceptions.RequestException: The API request could not be executed
      requests.exceptions.RequestException: There are errors in the call

  Returns:
      list[int]: category_ids_list
  """
  categories = []
  response = requests.get(url)

  if response.ok == False:
      raise requests.exceptions.RequestException("The API request could not be executed")
  
  data = json.loads(response.content)

  if 'errors' in data:
      raise requests.exceptions.RequestException("There are errors in the call")
  
  for result in data['results']:
     for category in result['categories']:
        categories.append(category['id'])

  return categories

def api_product_data_extractor_by_category(url_category, url_product, url_options, delay_time, category_ids_list:list[int]) -> list[dict]:
  """Extract all products for category list from mercadona api

  Args:
      url_category (str): API Category Mercadona URL.
      url_product (str): API Product Mercadona URL.
      url_options (str): API URL Options.
      delay_time (int): Delay time.
      category_ids_list (list[int]): Category ids list.

  Raises:
      ValueError: category_ids_list must have at least one element.

  Returns:
      list[dict]: product data collection
  """  

  if(len(category_ids_list) < 1):
     raise ValueError("category_ids_list must have at least one element.")

  product_data_collection = []

  for category in category_ids_list:
    url = url_category + str(category) + url_options

    response = requests.get(url)

    if response.ok == False:
      print("Error: The API request could not be executed")
      continue

    data = json.loads(response.content)

    if 'errors' in data:
      print("Error: Category was not found")
      continue
    
    if data['layout'] == 1:
      for category in data['categories']:

        print("Obtaining products from the category {}".format(category['name']))

        for product in category['products']:
            
            product = api_product_data_extractor(url_product, url_options, delay_time, product['id'])

            if(product == None):
               continue

            product['group_id'] = data['id']
            product['group_name'] = data['name']
            product['category_id'] = category['id']
            product['category_name'] = category['name']
            product_data_collection.append(product)

  return product_data_collection

def api_product_data_extractor(url_product, url_options, delay_time, product_id:int) -> dict | None:
  """ Gets the information of a product by its id

  Args:
      url_product (str): API Product Mercadona URL.
      url_options (str): API URL Options.
      delay_time (int): Delay time.
      product_id (int): Product id.

  Returns:
      dict | None: Data information
  """
  url = url_product + str(product_id) + url_options

  try:
    product_data = {}
    response = requests.get(url)

    if response.status_code == 401:
      print("Error 401: Token de autorización no válido")
      return
    
    if response.status_code == 404:
      print("Error 404: Producto no encontrado")
      return
    
    if response.status_code == 429:
      delay_time += 1
      print("Error 429: Reintentadolo con delay {}".format(delay_time))
      time.sleep(delay_time)
      api_product_data_extractor(url_product, url_options, delay_time, product_id)
      return

    if response.status_code != 200:
      print("Error desconocido: {}".format(response.status_code))
      return

    if response.status_code == 200:
      # Convertir los datos JSON de la respuesta en un dicc de Python
      data = json.loads(response.content)
      product_data['product_id'] = data['id']     
      product_data['product_brand'] = data['brand']
      product_data['product_pvp'] = data['price_instructions']['bulk_price']
      product_data['product_amount'] = data['price_instructions']['unit_size']
      product_data['product_unit'] = data['price_instructions']['size_format']
      product_data['product_price'] = data['price_instructions']['unit_price']

      if data['origin'] is not None:
          product_data['product_origin'] = data['origin'].replace(' ;', ',')
      else:
          product_data['product_origin'] = None

      product_data['product_description'] = data['details']['description']
      product_data['product_picture'] = data['photos'][0]['regular'].split('?')[0]

  except requests.exceptions.RequestException:
    print("Error: No se pudo realizar la petición a la API para el producto: {}".format(product_id))
    
  return product_data

def save_product_data_to_csv(data, file_path):
   
  with open(file_path, 'w', newline='', encoding='ISO-8859-1') as csv_file:

    field_names = ['group_id', 
              'group_name', 
              'category_id', 
              'category_name', 
              'product_id',
              'product_name',
              'product_brand', 
              'product_origin',
              'product_pvp',
              'product_amount',
              'product_unit',
              'product_price',
              'product_description',
              'product_picture']
    
    csv_writer = csv.DictWriter(
      csv_file, 
      delimiter=',',
      fieldnames=field_names,
      quotechar='"', 
      quoting=csv.QUOTE_MINIMAL)
    
    csv_writer.writeheader()
    
    for product in data:
       csv_writer.writerow(product)




