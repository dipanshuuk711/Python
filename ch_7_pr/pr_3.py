num = int(input("Enter the number to check if it's prime:\n"))
prime = True
for i in range(2,num):
    if num%2==0:
        prime = False
        break 
if prime:
   print("Entered number is prime")
else:
    print("Entered number is not prime")