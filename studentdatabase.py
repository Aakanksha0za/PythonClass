# -*- coding: utf-8 -*-
students = {
    "hero": "Batman",
    "lazy_guy": "Shinchan",
    "food_lover": "Doraemon"
}

print(" Original Dictionary:")
print(students)

students["coder"] = "Iron Man"

print("\n After Adding 'coder':")
print(students)

students.update({
    "topper": "Harry Potter",
    "sleeper": "Kumbhakarna"
})

print("\n After update() Function:")
print(students)

removed = students.pop("lazy_guy")

print(f"\n '{removed}' got removed using pop() because he skipped homework!")
print(students)

last_removed = students.popitem()

print(f"\n popitem() randomly kicked out: {last_removed}")
print(students)

del students["food_lover"]

print("\n After using del on 'food_lover':")
print(students)

students.clear()

print("\n After clear() Function:")
print(students)

print("\n School closed. No students left ")



