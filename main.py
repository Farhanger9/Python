# print("welcome to the name generator")
# city =input("Which did you grow up in? ")
# print(city)
# pet = input("what is your pet name?")
# print( "your band name is " + city +" " + pet)

# Day 2

# height = input("enter your height in m: ")
# weight = input("Enter your weight in kg: ")
# bmi = int(weight) / float(height) **2
# bmi_as_int = int(bmi)
# print (bmi_as_int)

#Final Project

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_person = bill_with_tip / people
final_amount = round(bill_person,2)
print(f"each person should pay {final_amount} dollar")




