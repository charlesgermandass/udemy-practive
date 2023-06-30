# import random
# import my_module


# random_integer = random.randint(1,100)

# print(str(random_integer) + " " + str(my_module.pi))

# random_float = random.random() *5
# print(random_float)

# # 1 Heads or Tails
# import random

# random_side = random.randint(0,1)

# if random_side == 1 :
#     print("Heads")
# else:
#     print("Tails")

# #Data List

# state_of_america =["Delaware","Pennsylvania"]

# print(state_of_america[0])

# print(state_of_america)

# print(state_of_america[-1])

# state_of_america[1] = "pencilvania"

# print(state_of_america)

# state_of_america.append("good")
# print(state_of_america)

# name1 = [ "a", "b", "c"]
# name2 = ["d", "e", "f"]

# names = [name1, name2]
# print(names)

# # Treasure Map
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# row = int(position[0])
# column = int(position[1])

# # selected_row = map[column-1]
# # selected_row[row-1] = "X"

# map[row-1][column-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

#Rock Paper Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images =[rock,paper,scissors]
#Write your code below this line 👇
user_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_Choice > 2 or user_Choice <0 :
    print("You typed a Invalid Number, You lose.")
else :
    print(f"You chose:\n" +game_images[user_Choice])

    Computer_Choice =random.randint(0,2)
    print(f"Computer chose:\n" +game_images[Computer_Choice])


    if user_Choice == 0 & Computer_Choice == 2 :
        print("You Win!")
    elif Computer_Choice == 0 & user_Choice == 2 :
        print("You lose!")
    elif Computer_Choice > user_Choice : 
        print ("You lose!")
    elif user_Choice > Computer_Choice : 
        print("You Win!")
    elif user_Choice == Computer_Choice :
        print("It's a draw")