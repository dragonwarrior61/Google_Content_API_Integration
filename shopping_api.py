from googleapiclient.discovery import build
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
            'content',
            config.API_VERSION,
            credentials=credentials,
            discoveryServiceUrl=config.DISCOVERY_URL,
            static_discovery=False
        )
        self.css_id = config.CSS_AGGREGATOR_ID
        self.shop_id = config.MERCHANT_ID

    def insert_product(self, product_data):
        print(product_data)
        try:
            start_time = datetime.now()
            request = self.service.products().insert(
                merchantId=self.shop_id,
                body=product_data
            )
            
            # Add the CSS header to the request
            request.headers["x-goog-merchant-id"] = self.css_id  # Your CSS ID (5579715225)
            
            # Execute the request
            product = request.execute()
            elapsed = (datetime.now() - start_time).total_seconds()
            
            logging.info(f"Successfully inserted product {product['id']} in {elapsed:.2f}s")
            print(f"Product inserted: {product['id']}")
            return product
            
        except Exception as e:
            logging.error(f"Error inserting product {product_data.get('offerId')}: {str(e)}")
            print(f"Error inserting product: {str(e)}")
            return None