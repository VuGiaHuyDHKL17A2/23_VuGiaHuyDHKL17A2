import xml.etree.ElementTree as ET

students = ET.Element('Students')

student1 = ET.SubElement(students, 'Student')
student1.set('id', '1')
ET.SubElement(student1, 'Name').text = 'Vu Gia Huy'
ET.SubElement(student1, 'YearOfBirth').text = '2005'
ET.SubElement(student1, 'Class').text = 'DHKL17A2'
ET.SubElement(student1, 'Gender').text = 'Male'

student2 = ET.SubElement(students, 'Student')
student2.set('id', '2')
ET.SubElement(student2, 'Name').text = 'PHAM NGOC THACH'
ET.SubElement(student2, 'YearOfBirth').text = '2001'
ET.SubElement(student2, 'Class').text = 'DHKL17A2'
ET.SubElement(student2, 'Gender').text = 'Female'

tree = ET.ElementTree(students)
tree.write('students.xml', encoding='utf-8', xml_declaration=True)

ET.dump(students)