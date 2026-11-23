print("Welcome to tip calculator!")
bill = float(input("What was the tota bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
split = float(input("How many people to split the bill? "))

tip = tip / 100

total = bill + (bill * tip)

perPerson = total / split


print(f"Each person should pay: ${perPerson:.2f}")
