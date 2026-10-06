#let's make guess num Game

import random

print("I am thinking a number between 1 to 20 ")

secretNum = random.randint(1,20)

#let user guess num 5 times 

for guessTaken in range(1,6):
    print("take a guess")
    
    guess = int(input())
    if guess < secretNum:
        print(" your guess is too low")
        
    elif guess > secretNum:
        print("your Guess is too high")  
        
    else:
        break   
    
if guess == secretNum:
    print(f' "WON!" you guessed the right num in {guessTaken} guess')  
    
else:
    print(f'"Loose!" you couldnt guess the right. right num is {secretNum}')        