from googleapiclient.discovery import build
from google.auth.transport.requests import AuthorizedSession
from auth import authenticate
import config

import logging
from datetime import datetime

logging.basicConfig(
    filename='shopping_api.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ShoppingContentAPI:
    def __init__(self):
        credentials = authenticate()
        self.service = build(
            'css',
            'v1',
            credentials=credentials,
            # static_discovery=False
        )
        self.css_id = config.CSS_AGGREGATOR_ID
        # self.shop_id = config.MERCHANT_ID

    def insert_product(self, product_data):
        print(product_data)
        try:
            parent = f"accounts/{self.css_id}"
                
            request = self.service.accounts().cssProductInputs().insert(
                parent=parent,
                body=product_data
            )
            response = request.execute()
            print(response)
            return response
            
        except Exception as e:
            logging.error(f"Error inserting product {product_data.get('offerId')}: {str(e)}")
            print(f"Error inserting product: {str(e)}")
            return None