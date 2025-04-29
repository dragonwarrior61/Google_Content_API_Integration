import xml.etree.ElementTree as ET
import requests

def parse_xml(url):
    response = requests.get(url)
    xml_content = response.content
    root = ET.fromstring(xml_content)
    
    products = []
    for item in root.findall('.//item'):
        product = {
            'name': item.find('g:title').text if item.find('g:title') is not None else None,
            'finalName': item.find('g:title').text if item.find('g:title') is not None else None,
            'rawProviderId': 'nl',
            'contentLanguage': item.find('g:price').text if item.find('g:price') is not None else None,
            'feedLabel': 'nl',
            'attributes': {
                'product_type': item.find('g:product_type').text if item.find('g:product_type') is not None else None,
                'link': item.find('link').text if item.find('link') is not None else None,
                'image_link': item.find('g:image_link').text if item.find('g:image_link') is not None else None,
                'condition': item.find('g:condition').text if item.find('g:condition') is not None else None,
                'availability': item.find('g:availability').text if item.find('g:availability') is not None else None,
                'price': item.find('g:price').text if item.find('g:price') is not None else None,
                'mpn': item.find('g:mpn').text if item.find('g:mpn') is not None else None,
                'brand': item.find('g:brand').text if item.find('g:brand') is not None else None,
                'google_product_category': item.find('g:google_product_category').text if item.find('g:google_product_category') is not None else None,
                'gtin': item.find('g:gtin').text if item.find('g:gtin') is not None else None,
                'canonical_link': item.find('g:canonical_link').text if item.find('g:canonical_link') is not None else None,
                'identifier_exists': item.find('g:identifier_exists').text if item.find('g:identifier_exists') is not None else None
            }
        }
        products.append(product)
    
    return products