import xml.dom.minidom
doc = xml.dom.minidom.parse("sample.xml")

company = doc.documentElement
company_name = company.getElementsByTagName("name")[0].childNodes[0].data
print("Tên công ty:", company_name)

staff_list = company.getElementsByTagName("staff")
for staff in staff_list:
    staff_id = staff.getAttribute("id")
    staff_name = staff.getElementsByTagName("name")[0].childNodes[0].data
    salary = staff.getElementsByTagName("salary")[0].childNodes[0].data
    print(f"Nhân viên ID {staff_id}: {staff_name}, Lương: {salary}")