# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_height = float(height) ** 2
bmi = int(weight) / new_height

if int(bmi) < 18.5:
    print("You are underweight")    
elif 25 > int(bmi) >= 18.5:
    print("Normal weight")
elif 30 > int(bmi) >= 25:
    print("You are slightly overweight")
elif 35 > int(bmi) >= 30:
    print("You are obese")
else:
    print("You are clinically obese")
    
# print(int(bmi))

