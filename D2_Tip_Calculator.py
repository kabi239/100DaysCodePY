# Tip Calculator
print("Welcome to the tip calculator. ") 
bill=float(input("What was the total bill? "))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? " ))
people=int(input("How many people to split the bill? "))
b_t=tip/100*bill+bill
b_p=b_t/people
print(f"Each person should pay: ${round(b_p,2)}")
