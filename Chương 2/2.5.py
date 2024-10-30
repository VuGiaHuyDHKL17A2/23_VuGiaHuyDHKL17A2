from xml.dom import minidom

doc = minidom.parse('sample.xml')
staffs = doc.getElementsByTagName('staff')

for staff in staffs:
    staff_id = staff.getAttribute('id')
    name = staff.getElementsByTagName('name')[0].firstChild.data
    salary = staff.getElementsByTagName('salary')[0].firstChild.data
    print(f'Staff ID: {staff_id}, Name: {name}, Salary: {salary}')