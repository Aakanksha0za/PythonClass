# -*- coding: utf-8 -*-
dictionary = {
    "name": "Aakanksha",
    "hobbies": ["Cycling", "Dancing"],
    "skills": ["Python", "Javascript"],
    "grade": 9,
    "school": "St.Mary's School"
}

print("About me:", dictionary)

dictionary["age"] = 14

print("\nUpdated Dictionary:")
print(dictionary)

dictionary.pop("skills")

print("\nDictionary:")
print(dictionary)

    

