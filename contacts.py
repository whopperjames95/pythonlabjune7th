contacts = {
    "number": 4,
    "students":
    [
        {"name": "Sarah Holderness", "email": "sara@example.com"},
        {"name": "James", "email": "james@example.com"},
        {"name": "tony", "email": "james@example.com"},
        {"name": "ron", "email": "ron@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])