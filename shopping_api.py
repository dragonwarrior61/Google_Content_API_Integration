from googleapiclient.discovery import build
from auth import authenticate
import config

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
        self.merchant_id = config.MERCHANT_ID

    def insert_product(self, product_data):
        try:
            product = self.service.products().insert(
                merchantId=self.merchant_id,
                body=product_data
            ).execute()
            print(f"Product inserted: {product['id']}")
            return product
        except Exception as e:
            print(f"Error inserting product: {str(e)}")
            return None