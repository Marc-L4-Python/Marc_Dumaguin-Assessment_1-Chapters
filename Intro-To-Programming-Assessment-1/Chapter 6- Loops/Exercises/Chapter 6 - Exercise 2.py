prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")


# This program/code uses the "prompt" function once again and asks for the user's age.
# Once the user enters their age/a number, the program prints a text that informs the user about the 
# price of their movie ticket based on their age. 
# If they enter the value "quit", then the whole program ends.