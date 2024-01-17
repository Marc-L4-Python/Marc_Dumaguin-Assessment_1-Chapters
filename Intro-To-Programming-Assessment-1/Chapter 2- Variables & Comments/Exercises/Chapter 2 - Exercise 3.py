name = "       Marc\tRommel\nS. Dumaguin   "
lstripped_name = name.lstrip(" Mar")
rstripped_name = name.rstrip("guin ")
stripped_name = name.strip()
#replaced_name = name.replace("\n", " ")           
         
# Was only testing out this function above '.replace()'. It is not part of the main activity but wanted to keep it in the code.


print ("\n", "Example Name: ", "\n", name, "\n"*2)
print ("Leading Stripped Name: ", "\n", lstripped_name, "\n"*2)
print ("Trailing Stripped Name: ", "\n", rstripped_name, "\n"*2)
print ("Stripped Name: ", "\n", stripped_name, "\n"*2)

print ("Original Name: ", "Marc Rommel S. Dumaguin",  "\n")


# Used my own name as the value for the variable "name" and added whitespaces before and after my name.
# Also used the functions "\t" and "\n" at least once.


# The first stripped function is "leading strip" and is used to remove/strip the characters " Mar" at the start of my name.
# The second stripped function is "trailing strip" and is used to remove the characters "guin " at the end of my name.
# The third and last stripped function is the normal "strip" function and is used to
# remove the whitespaces at the start and end of my name.


# Added the last print, "Original Name", just to show my whole name without the whitespaces, "\t", and "\n" functions.