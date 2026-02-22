import json
#JSON Syntax
{
  "name": "Alice",
  "age": 18
}

["apple", "banana", "cherry"]

{
  "student": {
    "name": "Bob",
    "grades": [85, 90, 88]
  }
}
{
  "is_active": true,
  "score": null
}
#Parsing JSON (json.loads())
import json

data = '{"name": "Alice", "age": 18}'
result = json.loads(data)
print(result)

json_str = '[1, 2, 3, 4]'
numbers = json.loads(json_str)
print(numbers)

json_str = '{"active": true}'
print(json.loads(json_str))

json_str = '{"student": {"name": "Bob", "age": 17}}'
print(json.loads(json_str)["student"]["name"])
#Converting Python to JSON (json.dumps())
import json

data = {"name": "Alice", "age": 18}
print(json.dumps(data))

numbers = [1, 2, 3]
print(json.dumps(numbers))
print(json.dumps(True))
data = {"a": 1, "b": None}
print(json.dumps(data))
#Writing JSON Files
import json

data = {"name": "Alice", "age": 18}
with open("data.json", "w") as f:
    json.dump(data, f)

data = {"active": True}
with open("active.json", "w") as f:
    json.dump(data, f, indent=4)

with open("empty.json", "w") as f:
    json.dump({}, f)
#Reading JSON Files
import json

with open("data.json", "r") as f:
    data = json.load(f)
print(data)

with open("numbers.json") as f:
    print(json.load(f))

with open("active.json") as f:
    print(json.load(f)["active"])
#Working with JSON data (sample-data.json in this folder)
{
  "students": [
    {"name": "Alice", "age": 18},
    {"name": "Bob", "age": 17}
  ]
}
print(data["students"])
print(data["students"][0]["name"])
for s in data["students"]:
    print(s["name"], s["age"])