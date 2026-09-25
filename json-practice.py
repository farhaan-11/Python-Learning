import json

text= '{"name": "John", "age": 30, "city": "New York", "skills": ["Python", "JavaScript", "SQL"]}'

# Parse JSON string to Python dictionary
data = json.loads(text)

print(data)

# print skills
print("skills:", data.get("skills"))

#  get title
print("title", data.get("title"))


#  create a new dictionary
new_data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles",
    "skills": ["Java", "C++", "HTML"]
}

#  convert into string

new_text = json.dumps(new_data)
print("string data:",new_text)
# print("type of new_text:", type(new_text))
# print("type of new_data:", type(new_data))

# print("name",new_text.get("name"))  # This will raise an error because new_text is a string, not a dictionary

print("name", new_data.get("name"))  # This will work because new_data is a dictionary
