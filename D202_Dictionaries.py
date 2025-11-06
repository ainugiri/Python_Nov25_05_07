# store : key and value
# dictionary : key and value
#  def: 

# a825662:{
#     name: 'Giri'
#     dept: 'lnd'
#     loc :' Chennai, In'
#     mov : 98512
# }

e1 = {
    'DAS_ID' : 'A825662',
    'Name' : 'Giri Prasad P',
    'Location' : 'Paris'
}

print(e1)
print(type(e1))


e2 = {"DAS_ID": "A825663", "Name":"Jackline", "Location":"London"}
print(e2)
print(type(e2))

print(f"{e2["Name"]} is from {e2['Location']}")
print(f"{e1["Name"]} is from {e1['Location']}")
e1['Name'] = "Afzal"
print(f"{e1["Name"]} is from {e1['Location']}")

e1["Mobile"] = 9840
print(e1)

e1["Mobile"] = 9840201202
print(e1)

print(e1.keys())

for key in e1.keys():
    print(key)

print(e1.values())

for v in e1.values():
    print(v)

e1["Name"] = "Giri Prasad P"

for k,v in e1.items():
    print(k,v)

print(len(e1))
# print(e1["age"])

print(e1.get("age"))