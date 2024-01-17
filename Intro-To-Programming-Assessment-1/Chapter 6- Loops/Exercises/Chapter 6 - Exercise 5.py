sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []
# List of sandwiches with 3 pastrami values and an empty list


print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# Message stating pastrami is out and removes the 3 pastrami values


print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
# Loop function that says that it is MAKING sandwiches


print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
# Loop function that says the FINISHED sandwiches