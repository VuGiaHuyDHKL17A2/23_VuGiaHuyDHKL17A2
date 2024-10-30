import json

json_data = '{"name": "Vu Gia Huy", "age": 20, "city": "Hanoi"}'
python_obj = json.loads(json_data)
print(python_obj)