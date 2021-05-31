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

list=[rock,paper,scissors]
num= random.randint(0,len(list)-1) #generate computer's choise

response= int(input("Enter your response:rock 0 or paper 1 or scissors 2: ")) #get user's choise
if response==0 or response==1 or response ==2:
  #declare final outcomes 
  won="You won!"
  lost="You lost!"
  tie="It's a tie!"

  print(list[response])#display user's choise
  print(list[num])#display computer's choise
  if response ==0:
    #print(f"{rock}\n ")
    if num==0:
      print(tie)
    elif num==1:
      print(won)
    elif num==2:
      print(lost)
    else:
      print("Error")
  elif response==1:
    #print(f"{paper}\n")
    if num==0:
      print(won)
    elif num==1:
      print(tie)
    elif num==2:
      print(lost)
    else:
      print("Error")
  else:
    #print(scissors)
    if num==0:
      print(lost)
    elif num==1:
      print(won)
    elif num==2:
      print(tie)
    else:
      print("Error")
else:
  print("Invalid input! You lost!")
