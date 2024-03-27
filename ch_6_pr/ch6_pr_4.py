#This will show you if entered username contains 10 character or not
username = input("Enter your UserName:\n")
# a = print(len(username))
# print(type(a))
# b = int(a)
# print(type(b))
if int(len(username))<10:
    print("Username contains less than 10 characters")
else:
    print("Hello",username)
