letter = '''Dear <name> \nYou are selected! \n<date>'''
a = input("Enter Your Name:")
b = input("Enter Date:")
letter=letter.replace("<name>",a)
letter=letter.replace("<date>",b)
print(letter)