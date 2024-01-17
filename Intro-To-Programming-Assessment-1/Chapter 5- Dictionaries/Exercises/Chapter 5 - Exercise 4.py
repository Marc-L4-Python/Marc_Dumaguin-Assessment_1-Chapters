rivers = {
    "Nile River": "Eastern Africa",
    "Amazon River": "South America",
    "Mississippi River": "Minnesota to Gulf of Mexico"
} # Dictionary of rivers and its location

# Loop function that prints the whole statement
for river, country in rivers.items():
    print ("The " + river.title() + " flows through " + country.title() + ".")

# Loop function that prints the rivers
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

# Loop function that prints the countries where the rivers are located
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())