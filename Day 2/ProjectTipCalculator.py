#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
print("Welcome to the tip calculator!")
bill = input("What was the total bill?  $") #string
tip = input("How much tip would you like to give? 10, 12 or 15? ") #string
split = input("How many people to split the bill? ")  #string

pay = (int(bill) / int(split)) * (int(tip)/100)
pay_round = round(pay, 2)
print(pay_round)