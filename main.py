from bs4 import BeautifulSoup
import requests
import pandas as pd
from pprint import pprint

BRAZIL_WIKI = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil"
PORTUGAL_WIKI = "https://pt.wikipedia.org/wiki/Lista_de_cidades_em_Portugal"

r_brazil = requests.get(BRAZIL_WIKI).text
brazil_soup = BeautifulSoup(r_brazil, "html.parser")
br_cities = brazil_soup.select("table tbody tr ul li a")[:-58]
br_cities = [city.text for city in br_cities]

r_portugal = requests.get(PORTUGAL_WIKI).text
portugal_soup = BeautifulSoup(r_portugal, "html.parser")
pt_cities = portugal_soup.select("table tbody tr td b a")
pt_cities = [city.text for city in pt_cities]

# scrapes two Wikipedia pages and outputs two lists with all cities from Brazil and Portugal

brazil_series = pd.Series(data=br_cities, name="brazilian_cities")
portugal_series = pd.Series(data=pt_cities, name="portugal_cities")

common_city = [city for city in pt_cities if city in br_cities]
common_series = pd.Series(data=common_city, name="same_name_cities")
common_series.to_csv("common_cities.csv", index=False)

# outputs a CSV file that contains city names that exist both in the Brazil city list and the Portugal city list
