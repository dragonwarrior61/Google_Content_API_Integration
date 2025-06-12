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
        if raw_price:
            value_str = raw_price.split()[0].replace('.', '').replace(',', '.')
            currency = raw_price.split()[-1]
            amount_micros = int(float(value_str) * 1_000_000)
            price = {"amount_micros": str(amount_micros), "currency_code": currency}
        else:
            price = None
            
        custom_label_text = item.find('g:custom_label_0', ns).text if item.find('g:custom_label_0', ns) is not None else None
        numberOfOffers = int(item.find('g:sell_on_google_quantity', ns).text) if item.find('g:sell_on_google_quantity', ns) is not None and item.find('g:sell_on_google_quantity', ns).text.isdigit() else None
        rawProvidedId = item.find('g:id', ns).text if item.find('g:id', ns) is not None else None
        title = item.find('g:title', ns).text if item.find('g:title', ns) is not None else None
        headlineOfferLink = item.find('link').text if item.find('link') is not None else None
        headlineOfferCondition = item.find('g:condition', ns).text if item.find('g:condition', ns) is not None else None
        description = item.find('g:description', ns).text if item.find('g:description', ns) is not None else None
        cppLink = item.find('g:canonical_link', ns).text if item.find('g:canonical_link', ns) is not None else None
        brand = item.find('g:brand', ns).text if item.find('g:brand', ns) is not None else None
        googleProductCategory = item.find('g:google_product_category', ns).text if item.find('g:google_product_category', ns) is not None else None
        gtin = item.find('g:gtin', ns).text if item.find('g:gtin', ns) is not None else None
        imageLink = item.find('g:image_link', ns).text if item.find('g:image_link', ns) is not None else None
        
        if custom_label_text == '0':
            continue
        
        if numberOfOffers is None:
            continue
        
        if numberOfOffers < 2:
            continue
        
        # if rawProvidedId is None:
        #     continue
        
        # if title is None:
        #     continue
        
        # if headlineOfferLink is None:
        #     continue
        
        # if headlineOfferCondition is None:
        #     continue
        
        # if description is None:
        #     continue
        
        # if cppLink is None:
        #     continue
        
        # if brand is None:
        #     continue
        
        # if googleProductCategory is None:
        #     continue
        
        # if gtin is None:
        #     continue
        
        # if imageLink is None:
        #     continue
        
        product = {
            "rawProvidedId": rawProvidedId,
            "feedLabel": "NL",
            "contentLanguage": "nl",
            "attributes": {
                "title": title,
                "headlineOfferLink": headlineOfferLink,
                "headlineOfferCondition": headlineOfferCondition,
                "description": description,
                "cppLink": cppLink,
                "brand": brand,
                "googleProductCategory": googleProductCategory,
                "gtin": gtin,
                "imageLink": imageLink,
                "headlineOfferPrice": price,
                # "customLabel0": custom_label_0,
                "numberOfOffers": str(numberOfOffers)
                # "certifications": [{
                #     "code": "12",
                #     "authority": "European Commission",
                #     "name": "EPREL"
                # }],
                # "productHighlights": [
                #     "test highlight"
                # ],
                # "productDetails": [{
                #     "sectionName": "test section",
                #     "attributeName": "test attribute",
                #     "attributeValue": "test value"
                # }]
            }
        }
        products.append(product)
        # break
    
    return products