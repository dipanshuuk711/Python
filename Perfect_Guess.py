import random
randNumber = random.randint(1,100)
# print(randNumber)
guess = 0 
userGuess = None
while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess:"))
    guess += 1
    if (userGuess == randNumber):
       print("You guessed it right! ")
    else:
        if(userGuess < randNumber):
         print("You guessed it wrong.Enter a larger number!")
        else:
            print("You guessed it wrong.Enter a smaller number!")
        print("You guessed it wrong")
    

print(f"You guessed in {guess} guesses") 
with open("a.txt", "r") as f:
    highscore = f.read()

if str(guess) < highscore:
    print("You just made a new highscore!")
      
    with open ("a.txt", "w") as f:
        f.write(str(guess))
    