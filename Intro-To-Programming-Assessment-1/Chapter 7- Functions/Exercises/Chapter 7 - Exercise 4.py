def make_shirt(size = "Large", message = "I love Python!"):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')
# Function that has large shirt as default size with a 
# default message

make_shirt()
make_shirt(size = "Medium")
make_shirt("Small", "Be Legendary.")
# Parameters that changes the shirt size and message