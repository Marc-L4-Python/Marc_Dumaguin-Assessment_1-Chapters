pets = [] # Empty list


pet = {
    "Animal Type": "Dog",
    "Name": "Edgar",
    "Owner": "Felix",
    "Weight": 10,
    "Eats": "Banana",
}
pets.append(pet)
# Dictionary for pet and pet details

pet = {
    "Animal Type": "Dog",
    "Name": "Puga-chan",
    "Owner": "Marzia",
    "Weight": 7,
    "Eats": "Meat",
}
pets.append(pet)
# Dictionary for pet and pet details

pet = {
    "Animal Type": "Cat",
    "Name": "Neko",
    "Owner": "Rie",
    "Weight": 3,
    "Eats": "Tuna",
}
pets.append(pet)
# Dictionary for pet and pet details


for pet in pets:
    print("\nHere's what I know about " + pet["Name"].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
# Loop function that prints the LIST, which takes its
# data from the DICTIONARY