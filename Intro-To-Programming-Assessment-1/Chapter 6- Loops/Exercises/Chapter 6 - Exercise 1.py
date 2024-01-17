prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break


# This program uses a "prompt" function which indicates that the program can obtain a value or information
# from the user, which in this case is a pizza topping. It then uses that prompt for a loop that informs
# the user that the topping will be put onto their pizza until they enter the value "quit", which stops the program.