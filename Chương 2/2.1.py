import xml.etree.ElementTree as ET
company = ET.Element('Company')
director = ET.SubElement(company, 'Director')
director.text = 'Vu Gia Huy'
address = ET.SubElement(company, 'Address')
address.text = '218 Linh Nam'
phone = ET.SubElement(company, 'Phone')
phone.text = '0123456789'
tax_code = ET.SubElement(company, 'TaxCode')
tax_code.text = '123456789'
tree = ET.ElementTree(company)
tree.write('company_info.xml', encoding='utf-8', xml_declaration=True)
ET.dump(company)