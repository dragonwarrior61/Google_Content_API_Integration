import xml.etree.ElementTree as ET
import requests
import pandas as pd

def parse_xml(xml_content):
    """Parse the XML content and extract product information"""
    root = ET.fromstring(xml_content)
    
    products = []
    for item in root.findall('.//item'):
        product = {
            'id': item.find('g:id').text if item.find('g:id') is not None else None,
            'title': item.find('g:title').text if item.find('g:title') is not None else None,
            'price': item.find('g:price').text if item.find('g:price') is not None else None,
            'brand': item.find('g:brand').text if item.find('g:brand') is not None else None,
            'product_type': item.find('g:product_type').text if item.find('g:product_type') is not None else None,
            'image_link': item.find('g:image_link').text if item.find('g:image_link') is not None else None,
            'link': item.find('link').text if item.find('link') is not None else None,
            'gtin': item.find('g:gtin').text if item.find('g:gtin') is not None else None,
            'mpn': item.find('g:mpn').text if item.find('g:mpn') is not None else None,
            'availability': item.find('g:availability').text if item.find('g:availability') is not None else None,
            'description': item.find('g:description').text if item.find('g:description') is not None else None
        }
        products.append(product)
    
    return products

# Option 1: Load from URL
url = "https://wasje.nl/wp-content/uploads/woo-feed/google/xml/shopping.xml"
response = requests.get(url)
xml_content = response.content

# Option 2: Use local XML string (like your example)
# xml_content = """your xml string here"""

products = parse_xml(xml_content)

# Convert to DataFrame for analysis
df = pd.DataFrame(products)

# Clean price data (convert to float)
df['price'] = df['price'].str.replace(' EUR', '').str.replace('.', '').str.replace(',', '.').astype(float)

# Extract capacity from title (example pattern)
df['capacity_kg'] = df['title'].str.extract(r'(\d+)\s?kg', flags=re.IGNORECASE)

print(f"Found {len(df)} products")
print(df.head())

# Save to CSV
df.to_csv('wasje_products.csv', index=False)
print("Saved to wasje_products.csv")

# Basic analysis
print("\nPrice Statistics:")
print(df['price'].describe())

print("\nTop Brands:")
print(df['brand'].value_counts())