class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the Programmer is {self.name} and Product's name is {self.product}")    
dipanshu = Programmer("Dipanshu", "Edge")
bottle = Programmer("Bottle", "Github")
dipanshu.getInfo()