import json

python_obj = {'name': 'Vu Gia Huy', 'age': 22, 'city': 'Hanoi'}
json_data = json.dumps(python_obj, indent=4)
print(json_data)