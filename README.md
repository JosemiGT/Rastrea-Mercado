***

_Este repositorio muestra el proyecto realizado para la entrega de la
**Práctica 1** de la asignatura **Tipología y Ciclo de Vida de los Datos (M2.851)** del
Máster universitario de Ciencia de Datos (UOC)._

***

# Práctica 1 - Tipología y Ciclo de Vida de los Datos

Asignatura: M2.851 / Semestre: 2023-2 / Fecha: 15-04-2023

URL del sitio web elegido: https://tienda.mercadona.es/

## Autores

  * Salvador Pulido Sánchez - [spulidos@uoc.edu](spulidos@uoc.edu)
  * José Miguel Gamarro Tornay - [josemigt@uoc.edu](josemigt@uoc.edu)

## Descripción del repositorio

Breve desripción de la práctica/sitio web elegido.

  * `memoria.pdf`: Documento de respuestas.
  * `/source/scraper/MercadonaScraper.py`: Clase para controlar la nevegación en la página de mercadona mediante selenium para obtener información.
  * `/source/models/product.py`: Clase modelo de producto para guardar la información.
  * `/source/repository/CSVProductRepository.py`: Clase de repositorio para guardar los productos en un fichero CSV.
  * `/source/scraper_api/scraper.py`: Módulo que contiene la lógica para obtener datos de productos desde la API.
  * `/source/scraper_api/scraper_aux.py`: Módulo que contiene funciones auxiliares que se utilizan en scraper.py para obtener información mediante la API de mercadonaI.
  * `/source/requirements.txt`: Lista de paquetes utilizados (Python 3.10).
  * `/dataset/20230424_datos_mercadona.csv`: DataSet con todos el conjunto de datos obtenido de los productos de la web de mercadona.
  * `/dataset/20230424_datos_mercadona_api.csv`: DataSet con todos el conjunto de datos obtenido de los productos de la api de mercadona.

## Publicación en Zenodo

El dataset ha sido publicado en Zenodo con DOI [10.5281/zenodo.7864593](https://doi.org/10.5281/zenodo.7864593).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7864593.svg)](https://doi.org/10.5281/zenodo.7864593)

## Vídeo de presentación

Enlace al vídeo de presentación de la práctica: [https://drive.google.com/file/d/1t9pVGXzJNzeS9a2oXhKAN6pbT0CDFsNP/view?usp=share_link](https://drive.google.com/file/d/1t9pVGXzJNzeS9a2oXhKAN6pbT0CDFsNP/view?usp=share_link)
