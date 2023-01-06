print("Welcome to tip calculator!")
bill = float(input("What was the bill? "))
tip = float(input("What percentage tip would you like to give 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# find the price of the tip 
tip_price = (tip /100) * bill
print(tip_price)