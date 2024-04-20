students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

# for student in students:
#     for key, value in student.items():
#         print(f"{key} -> {value}")
#     print("-------------")

print("-------------")

for student in students:
    print(f"{student['name']} | {student['house']} | {student['patronus']}")