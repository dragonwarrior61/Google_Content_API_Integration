from shopping_api import ShoppingContentAPI
from data_processing import parse_xml
import time

def main(url):
    api = ShoppingContentAPI()
    
    products = parse_xml(url)
    
    print(len(products))
    for product in products:
        result = api.insert_product(product)
        time.sleep(0.1)
    print(result)
    
    
if __name__ == "__main__":
    url = "https://wasje.nl/wp-content/uploads/woo-feed/google/xml/shopping.xml"
    main(url)