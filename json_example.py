import json

user = """
{
  "name": "Akella",
  "age": 25,
  "is_student": true,
  "courses": [
    "Python",
    "QA Engineer",
    "API Testing"
  ],
  "address": {
    "city": "Inno",
    "region": "Tat",
    "zip": 640500
  }
}
"""
parsed_data = json.loads(user)

parsed_data["name"] = "Petr"
parsed_data["age"] = 15

# json_str = json.dumps(parsed_data, indent=4)
# print(json_str, type(json_str))

with open(file="example.json", encoding="utf-8") as f:
    data = json.load(f)
    print(data)

with open(file="example_2.json", mode="w", encoding="utf-8") as fw:
    json.dump(parsed_data, fw, ensure_ascii=False, indent=4)