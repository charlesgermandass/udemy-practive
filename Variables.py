# # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# Years_have = 90-int(age)
# Days_have = 365 * Years_have
# Weeks_have = 52* Years_have
# Moths_have = 12 * Years_have

# print(f"You have {Days_have} days, {Weeks_have} weeks, and {Moths_have} months left.")


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the top calculator!")
bill =float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

bill_with_tip =tip/100 *bill + bill

bill_per_person = bill_with_tip /people

#final_amount =round(bill_per_person,2)

final_amount = "{:.3f}".format(bill_per_person)

print(f"Each person should pay $ {final_amount}")
