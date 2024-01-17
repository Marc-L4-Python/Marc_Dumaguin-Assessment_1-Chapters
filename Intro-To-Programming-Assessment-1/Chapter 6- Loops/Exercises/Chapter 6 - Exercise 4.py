sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# List of sandwiches
finished_sandwiches = []
# Empty list for finished sandwiches

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
# Loop function that says that it is MAKING sandwiches

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
# Loop function that says the FINISHED sandwiches