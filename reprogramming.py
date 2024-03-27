import random
randnu = random.randint(1,100)
guess = 0
you = None

while randnu != you:
    you = int(input("Enter your number: "))
    guess += 1
    if you == randnu:
        print("You guess it right...")
        print(f"You guessed in {guess} tries...")
    elif you > randnu:
        print("You guessed it wrong.Enter a smaller number..")
    elif you < randnu:
        print("You guessed it wrong.Enter a larger number...")    
    else:
        print("You guessed it wrong...")

with open ("a.txt",'r') as f:
   hiscore = f.read()

if int(hiscore) > guess:
    print("You just made a new hiscore")
    
with open ("a.txt",'w') as f:
    f.write(str(guess))