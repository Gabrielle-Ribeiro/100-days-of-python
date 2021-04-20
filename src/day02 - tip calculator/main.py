print("Welcome to the bill calculator!")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percetage tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

bill_with_tip = bill + bill * (percentage_tip/100)
total = bill_with_tip / number_of_people

print("Each person should pay ${:.2f}".format(total))