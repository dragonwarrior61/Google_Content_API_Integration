import xml.etree.ElementTree as ET
import requests

def parse_xml(url):
    response = requests.get(url)
    xml_content = response.content
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