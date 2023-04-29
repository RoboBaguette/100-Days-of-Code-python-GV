# Tip calculator prompt
print("Welcome to the tip calculator.")
# inputs from user
b = input("What was the total bill? $")
n = input("How many people are splitting the bill? ")
t = input("What percentage tip would you like to give? 10, 12 or 15? ")
# Converting Datatypes
bill, num_p, tip_p = float(b), float(n),float(t)
# Calculating tip amount and converting it in to a string
bill_p = bill/num_p
pay = bill_p*(1 + (tip_p/100))
pay = round(pay, 2)
pay = str(pay)
# displaying what each person should pay
print("Each person should pay: " + pay)