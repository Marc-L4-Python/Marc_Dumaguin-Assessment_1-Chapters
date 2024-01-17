glossary = {"Algorithm": "a set of instructions that are executed to get the solution to a given problem.", 
            "Variable": "a reserved memory location to store values.", 
            "Value": "a sequence of bits that is interpreted according to some data type.", 
            "Data Types": "the classification or categorization of knowledge items.", 
            "Operators": "special symbols, combinations of symbols, or keywords that designate some type of computation.",
            "String": "a series of characters.",
            "Comment": "a note in a program that the Python interpreter ignores.",
            "Loop": "work through a collection of items, one at a time.",
            "Float": "a numerical value with a decimal component.",
            "Dictionary": "a collection of key-value pairs.",
            } # Dictionary consisting of 5 python terms I learned and added 5 more


for word, definition in glossary.items():
    print("\n" + word.title() + " - " + definition)
# A loop function that prints the whole dictionary.
# It prints the title and definition