cities = ["Tokyo", "Seoul", "Bern", "Paris", "Rome"] # List of cities/places

print("\n",cities) # Normal print

print("\n", sorted(cities)) # Prints alphabetically
print("", cities)

print("\n", sorted(cities, reverse=True)) # Prints alphabetically
print("", cities)                         # and reversed order

cities.reverse() # Reverses the order of items in list
print("\n", cities)

cities.reverse() # Reverse the list again, so back to
print("", cities) # normal order

cities.sort() # Prints alphabetically
print("\n", cities)

cities.sort(reverse = True) # Prints alphabetically
print("", cities, "\n") # and in reverse order