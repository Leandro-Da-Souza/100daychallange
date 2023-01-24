#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

bill = float(input("what was the total bill?\n$"))

tip = int(input("how much tip would you like to give? 10, 12, or 15?\n"))

people = int(input("how many people in the party?\n"))

bill_with_tip = bill * (1 + tip / 100)

tip_per_person = "{:.2f}".format(bill_with_tip / people, 2)
print(f"${tip_per_person}")