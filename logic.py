import random
from art import logo
print(logo)
lives=0
playing=True
# Allow the player to submit a guess for a number between 1 and 100.
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="easy":
  lives+=10
  print("You have 10 attempts reamining to guess the number.")
elif difficulty=="hard":
  lives+=5
  print("You have 5 attempts remaining to guess the number.")
else:
  print("You did not choose a valid difficulty.")

truenumber=random.randint(0,100)

while playing==True:
  guess=int(input("Make a guess: "))
# Check user's guess against actual answer.
  if guess > truenumber:
    print("Too high.")
    lives-=1
    print(f"You have {lives} attempts remaining to guess the number.")
  elif guess < truenumber:
    print("Too low.")
    lives-=1
    print(f"You have {lives} attempts remaining to guess the number.")
  else:
    print(f"You have guessed correctly! The true number was {truenumber} and you had {lives} attempts left.")
    playing=False
  if lives == 0:
    print("You have have used all your attempts. Try again next time!")
    playing=False

