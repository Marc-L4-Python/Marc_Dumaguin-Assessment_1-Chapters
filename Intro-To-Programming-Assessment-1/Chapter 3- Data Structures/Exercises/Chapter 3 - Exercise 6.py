invite_anyone = ["Michael Jordan", "Kobe Bryant", "LeBron James"] # List of invitees

print ("\n", "I cordially invite you to dinner at my home, Mr. " + invite_anyone[0], "\n", # Prints a message or
       "I cordially invite you to dinner at my home, Mr. " + invite_anyone[1], "\n",       # invitation for the invitees.
       "I cordially invite you to dinner at my home, Mr. " + invite_anyone[2], "\n"
       )

print ("", "Mr. " + invite_anyone[1] + " will not be able to make it to the dinner.") # Person can not attend

del(invite_anyone[1]) # Removes the person that can't attend
invite_anyone.insert (1, "Stephen Curry") # Insert new invitee

print ("\n", "I cordially invite you to dinner at my home, Mr. " + invite_anyone[0], "\n", # Prints an invitation
       "I cordially invite you to dinner at my home, Mr. " + invite_anyone[1], "\n",       # for the new list
       "I cordially invite you to dinner at my home, Mr. " + invite_anyone[2], "\n"
       )

print ("", "Sorry for the inconvenience Mr. " + invite_anyone[2], ",but we can only invite two people now.")
invite_anyone.pop(2) # Message that says 1 can not join and removes them

print ("\n Mr.", invite_anyone[0] + ", you are still invited to the dinner.", # Statements that says
       "\n Mr.", invite_anyone[1] + ", you are still invited to the dinner."  # 2 people are still invited
)

del(invite_anyone[0]) # Clears and removes the
del(invite_anyone[0]) # items in list

print (" \n", invite_anyone, "<-- Empty List", "\n") # Prints the empty list