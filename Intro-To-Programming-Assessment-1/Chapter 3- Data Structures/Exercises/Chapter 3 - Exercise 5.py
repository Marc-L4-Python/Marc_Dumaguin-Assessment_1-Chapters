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