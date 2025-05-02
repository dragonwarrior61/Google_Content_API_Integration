import xml.etree.ElementTree as ET
import requests

def parse_xml(url):
    response = requests.get(url)
    xml_content = response.content
    root = ET.fromstring(xml_content)
    
    ns = {'g': 'http://base.google.com/ns/1.0'}
    
    products = []
    for item in root.findall('.//item'):
        # print(ET.tostring(item, encoding='unicode'))
        raw_price = item.find('g:price', ns).text if item.find('g:price', ns) is not None else None
        
        print(raw_price)
        if raw_price:
            value = raw_price.split()[0].replace('.', '').replace(',', '.')
            currency = raw_price.split()[-1]
            price = {"value": value, "currency": currency}
        else:
            price = None
        
        product = {
            'id': item.find('g:id', ns).text if item.find('g:id', ns) is not None else None,
            'offerId': item.find('g:id', ns).text if item.find('g:id', ns) is not None else None,
            'title': item.find('g:title', ns).text if item.find('g:title', ns) is not None else None,
            'description': item.find('g:description', ns).text if item.find('g:description', ns) is not None else None,
            'link': item.find('link').text if item.find('link') is not None else None,
            'imageLink': item.find('g:image_link', ns).text if item.find('g:image_link', ns) is not None else None,
            'contentLanguage': 'nl',
            'feedLabel': 'NL',
            'condition': item.find('g:condition', ns).text if item.find('g:condition', ns) is not None else None,
            'availability': item.find('g:availability', ns).text if item.find('g:availability', ns) is not None else None,
            'price': price,
            'mpn': item.find('g:mpn', ns).text if item.find('g:mpn', ns) is not None else None,
            'brand': item.find('g:brand', ns).text if item.find('g:brand', ns) is not None else None,
            'google_product_category': item.find('g:google_product_category', ns).text if item.find('g:google_product_category', ns) is not None else None,
            'gtin': item.find('g:gtin', ns).text if item.find('g:gtin', ns) is not None else None,
            'channel': 'online'
        }
        products.append(product)
        break
    
    return products