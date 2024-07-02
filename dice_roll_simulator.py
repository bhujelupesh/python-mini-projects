import random

def diceroll():
  value = random.randint(1,6)
  return value

while True:
  choice = input("Want to roll the dice?(y/n)").lower()
  if choice == 'y':
    print(f"you rolled : {diceroll()}")
  elif choice == 'n':
    print("Thank you for playing!!!!")
    break
  else:
    print("Invalid Input!!! Please enter either 'y' or 'n' ")
