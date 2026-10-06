import random



secretNum = random.randint(0, 20);
print("I am thinking a number between 0 to 5")
# print(secretNum)

for guessTaken in range(1,):
    print("take a guess")
    guess = int(input())
    
    if guess< secretNum:
        print("your guessed num is too low")
    elif guess> secretNum:
        print("your guessed num is too high")
    else:
        break

if guess == secretNum:
    print(f"you guessed the number in {str(guessTaken)} guesses") 
else:
    print(f"you couldn't guess the right num , right num is {str(secretNum)} ")               
    

