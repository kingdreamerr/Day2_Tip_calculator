print("Welcome to tip calculator!")
bill = float(input("What was the bill? $"))
tip = float(input("What percentage tip would you like to give 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# find the price of the tip 
tip_price = (tip /100) * bill

# total price of the bill
bill_tip = bill + tip_price
bill_per_person = bill_tip / people
total_bill = round(bill_per_person,2)
total_bill = "{:.2f}".format(total_bill)
print(f"Each person should pay: ${total_bill}")