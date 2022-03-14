# Define a list of names
names = ["kim", "lee", "park", "choi"]

names.append("kang")
names.sort(reverse=False)
names.remove("choi")

print(names)
print(f"The list has {len(names)} elements.")
