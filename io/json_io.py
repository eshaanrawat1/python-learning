import json

def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for entry in data:
            print(entry["name"], entry["city"])

read_json("data/json1.json")
# Maya Chen Seattle
# Omar Haddad Chicago
# ...


json_string = '[{"id": 1, "name": "Maya Chen", "city": "Seattle", "age": 34, "active": true}, {"id": 2, "name": "Omar Haddad", "city": "Chicago", "age": 41, "active": true}]'
json_invalid = 'aks188\2'

def read_json2(s):
    try:
        data = json.loads(s)
        for entry in data:
            print(entry["name"], entry["city"])
    except json.JSONDecodeError as e:
        print(e)

read_json2(json_string)
# Maya Chen Seattle
# Omar Haddad Chicago

read_json2(json_invalid)
# Expecting value: line 1 column 1 (char 0)
    