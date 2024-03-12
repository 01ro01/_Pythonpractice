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


game_images = [rock,paper,scissors]

person_1 = int(input("WHAT DO YOU WANNA CHOOSE? \n 0/Rock\n 1/Paper\n 2/Scissors\n"))
print(game_images[person_1])
person_1 = random.randint(0, 2)

person_2 = int(input("WHAT DO YOU WANNA CHOOSE?\n 0/Rock\n 1/Paper\n 2/Scissors\n"))
print(game_images[person_2])
person_2 = random.randint(0, 2)

if person_1 >= 3 or person_2 < 0:
    print("You typed an invalid number.")
elif person_1 == 0 and person_2 == 2:
    print("Person1 WINS!!!\nPerson2 LOSES!!!")
elif person_1 == 0 and person_2 == 2:
    print("Person1 LOSES!!!\nPerson2 WINS!!! ")
elif person_1 > person_2:
    print("Person1 LOSES!!!\nPerson2 WINS!!!")
elif person_2 > person_1:
    print("Person1 WINS!!!\nPerson2 LOSES!!! ")
elif person_1 == person_2:
    print("GAME DRAW")
else:
    print("---YOU ARE OUT OF THE GAME.---")