Girl_mny_pnds = 50
USB_Stick_price = 6

USB_amt = Girl_mny_pnds//USB_Stick_price                    # Floor Division Arithmetic Operator
pnds_left = Girl_mny_pnds%USB_Stick_price                   # Modulus Arithmetic Operator

print("\n", "The girl can buy", USB_amt, "USB sticks.", "\n "
      "And she will have", pnds_left ,"Sterling Pounds left.", "\n")


# Used the "floor division operator" to solve and find the amount of USB sticks the girl can buy 
# and used the "modulus operator" to calculate how many pounds she will have left.

# Assigned two different variables for the "50 pounds of money" the girl has and the price of a
# USB stick, which is "6 pounds" each. Both of these variables are then used in the formula 
# for 2 new variables: 1) "USB_amt" for calculating the amount of USB sticks that can be bought 
# and 2) "pnds_left" to calculate how many pounds she will have left after buying.