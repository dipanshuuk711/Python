import random

def game(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False    

print("Comp's turn:Rock(r),Paper(p) or Scissor(s)")       
randomno = random.randint(1,3) 
if randomno == 1:
    comp = 'r'
elif randomno == 2:
    comp = 'p'
elif randomno == 3:
    comp = 's'
you = input("Rock(r),Paper(p) or Scissor(s):\n")
print("You chose:",you)
print("Comp chose:",comp)
a = game(comp,you)
if a == True:
    print("You Win!")
elif a == False:
    print("You Lose!")
elif a == None:
    print("This game is a tie!")
