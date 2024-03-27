#This syntax will create an empty dictinary and not an empty set

a = {}
print(1, type(a))
#An empty set can be created using below syntax-
b = set()
b.add(2)
b.add(8)
b.add(9)
b.add(53)
b.add((3,4,7,94,5))

print(2,type(b),b,len(b)) #len = prints the length of a set

b.remove(8) #removes 8 from the set
# b.remove(15) #it will throw an error because 15 is not present in the set
print(b.pop())
print(b)
