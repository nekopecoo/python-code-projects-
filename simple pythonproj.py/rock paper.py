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
image=[rock,paper,scissors]
user_choose=int(input("what do you choose?0 for rock, 1 for paper,2 for scissors"))
if user_choose>=0 and user_choose<=2:
    print(image[user_choose])

computer_choice=random.randint(1,4)
print(f"computer choose{computer_choice}")
if computer_choice>=0 and computer_choice<=2:
    print(image[computer_choice])

if computer_choice==0 and user_choose==2:
    print("you lose!")
elif user_choose==0 and computer_choice==2:
    print("you win!")
elif user_choose>computer_choice:
    print("you win!")
elif computer_choice>user_choose:
    print("you lose!")
elif computer_choice==user_choose:
    print("draw!")
elif user_choose>=3 or user_choose<0:
    print("you typed invalid number. you lose!")