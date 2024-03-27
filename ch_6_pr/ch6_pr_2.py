a = int(input("Enter the marks of physics: "))
b = int(input("Enter the marks of maths:"))
c = int(input("Enter the marks of Chemistry: "))
if(a<33 or b<33 or c<33):
    print("You failed because you ave less than 33 marks.")
elif(a+b+c)/3 <40:
    print("You failed, because you have less than 40% marks")    
else:
    print("you pass")
    