from shopping_api import ShoppingContentAPI

def main():
    api = ShoppingContentAPI()
    
    result = api.insert_product(product)
    print(result)
    
    
if __name__ == "__main__":
    main()