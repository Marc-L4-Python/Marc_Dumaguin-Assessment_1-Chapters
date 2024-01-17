def describe_city(city, country = "Japan"):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)
# Function that accepts and prints a city and country

describe_city("Tokyo")
describe_city("Bern", "Switzerland")
describe_city("Osaka")
# Two parameters that are used for the print 
# and one parameter that changes the one print output