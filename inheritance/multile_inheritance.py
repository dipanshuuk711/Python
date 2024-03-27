class Employee:
    company = "Visa"
    eCode = 120
class Freelancer:
    comapany = "Fiver"
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1
class Programmer(Employee, Freelancer):
    name = "Deepanshu"

p = Programmer()
p.upgradeLevel()
print(p.company)
