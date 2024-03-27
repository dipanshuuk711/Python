a = {
"laptop":"a small portable pc.", 
"Dipanshu":"It's my name"  
}
b = {
    "horse":"an animal",
    "sunglasses":"eyewear",
    "fan":"an electronic tool.",
    "Dipanshu":"A human name"
}


print(list(a.keys()))

a.update(b)
print(a["Dipanshu"])
print(type(a))
print(a.values())
# print(a.get("Dipanshu"))  #prints value assosiated with key "Dipanshu"
#The difference between ".get" and "[]" syntax
print(a.get("Dipanshu2"))   #returns none
# print(a["Dipanshu2"]) #throw an error as Dipanshu2 is not present in the list a...