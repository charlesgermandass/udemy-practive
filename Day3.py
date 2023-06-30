# #1 Roller Coaster
# print("Welcome t the rollercoaster")
# height = int(input("What is your height in cm? "))
# bill_amount =0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age <12:
#         bill_amount =5
#         print("Child tickets are $5.")
#     elif age <=18:
#         bill_amount =7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill_amount =12
#         print("Adult tickets are $12.")
#     wants_photo =input("Do you want a photo taken? Y or N.")
#     if wants_photo =="Y":
#         bill_amount += 3      
#     print(f"Your final bill is {bill_amount}")
# else:
#     print("Sorry, you have to grow taller before you can ride,")

# #2 
# number_entered = int(input("Which number do you want to check : "))
# if number_entered%2 ==0:
#     print("This is an even number.")    
# else:
#     print("This is an odd number.")

# #3 BMI 2.0
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# int_height = float(height)
# int_weight = float(weight)


# # result = int_weight /  (int_height*int_height)

# Bmi = round(int_weight / int_height ** 2)

# print(int(Bmi))

# if Bmi <18.5:
#     print(f"Your bmi is {Bmi}, you are underweight.")
# elif Bmi < 25:
#     print(f"Your bmi is {Bmi}, you are normal weight.")
# elif Bmi <30:
#     print(f"Your bmi is {Bmi}, you are overweight.")
# elif Bmi < 35:
#     print(f"Your bmi is {Bmi}, you are obese.")
# else:
#     print(f"Your bmi is {Bmi}, you are Clinically obese.")

# #4 Leap Year
# year = int(input("Which year do you want to check?"))

# if year % 4 ==0:
#     if year %100 ==0:
#         if year %400 ==0:
#             print("Leap Year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

# #5 Pizza order
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bill_amount = 0

# if size == "S":
#     bill_amount += 15
# elif size == "M":
#     bill_amount += 20
# elif size == "L":
#     bill_amount += 25

# if add_pepperoni == "Y":
#    if size == "S":
#      bill_amount += 2
#    else:
#      bill_amount += 3

# if extra_cheese == "Y":
#     bill_amount += 1

# print(f"Your final bill is: ${bill_amount}")

# #6 Love Score
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# lower_name1 = name1.lower()
# lower_name2 = name2.lower()

# true_score_name1 = 0
# love_score_name1 = 0

# true_score_name1 = lower_name1.count("t") 
# true_score_name1 += lower_name1.count("r")
# true_score_name1 += lower_name1.count("u")
# true_score_name1 += lower_name1.count("e")

# love_score_name1 += lower_name1.count("l")
# love_score_name1 += lower_name1.count("o")
# love_score_name1 += lower_name1.count("v")
# love_score_name1 += lower_name1.count("e")

# true_score_name2 = 0
# love_score_name2 = 0

# true_score_name2 = lower_name2.count("t") 
# true_score_name2 += lower_name2.count("r")
# true_score_name2 += lower_name2.count("u")
# true_score_name2 += lower_name2.count("e")

# love_score_name2 += lower_name2.count("l")
# love_score_name2 += lower_name2.count("o")
# love_score_name2 += lower_name2.count("v")
# love_score_name2 += lower_name2.count("e")

# final_true_score = true_score_name1 + true_score_name2
# final_love_score = love_score_name1 +love_score_name2

# final_score = str(final_true_score) +str(final_love_score)
# int_final_score = int(final_score)
# print(int_final_score)

# if int_final_score < 10 or int_final_score >90:
#     print(f"Your score is {int_final_score}, you go together like coke and mentos.") 
# elif int_final_score >40 and int_final_score <50:
#     print(f"Your score is {int_final_score}, you are alright together.") 
# else:
#     print(f"Your score is {int_final_score}.") 

#7 Treasure Island Game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("Do you want to go to left or right?").lower()
if direction != "left":
    print("Fall into a hole.\nGame Over.")
else:
    swimorwait = input("Swim or wait?").lower()
    if swimorwait != "wait":
        print("Attacked by trout.\nGame Over.")
    else:
        doorcolour = input("Which color door do you want to go!").lower()
        if doorcolour == "red":
            print("Burned by fire.\nGame Over.")
        elif doorcolour == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif doorcolour =="yellow":
            print("You Win!")
        else:
            print("Game Over.")

            

            



