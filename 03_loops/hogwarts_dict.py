students = {
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Hermione": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    # only prints dict keys
    print(f"{student}")

print("--------------")

for student in students:
    print(f"{student} -> {students[student]}")

print("--------------")

for key, value in students.items():
    print(f"{key} -> {value}")
