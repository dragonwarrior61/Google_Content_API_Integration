from shopping_api import ShoppingContentAPI
from data_processing import parse_xml
from time import time

def main(url):
    api = ShoppingContentAPI()
    
    products = parse_xml(url)
    for product in products:
        result = api.insert_product(product)
        time.asleep(0.1)
    print(result)
    
    
if __name__ == "__main__":
    url = "https://wasje.nl/wp-content/uploads/woo-feed/google/xml/shopping.xml"
    main(url)