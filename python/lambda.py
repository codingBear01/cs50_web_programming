people = [
    {"name": "Yoon", "nationality": "Korea"},
    {"name": "Biden", "nationality": "USA"},
    {"name": "Kishida", "nationality": "Japan"},
]


# def f(person):
#     return person["nationality"]
# people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)
