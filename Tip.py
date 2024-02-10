#Making a tip calculator
#Round the result in 2 decimal number

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? /- "))
tip = int(input("how much tip you want to give? 5,10 or 15? "))
people = int(input("How many people to split the the bill? "))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount 
bill_per_person = total_bill / people 

final_amount = "{: .2f}".format(bill_per_person)
print(f"Each person should pay {final_amount}/-")