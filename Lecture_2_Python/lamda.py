people = [
    {"name":"Jeet", "house":"pakhanjoor"},
    {"name":"Honey", "house":"Kanker"},
    {"name":"Drago", "house":"Jagdalpur"},
]

def fun (person):
    return person["name"]


# people.sort(key=fun)


people.sort(key=lambda person:person["name"])
print(people)

# defining function in one lne 