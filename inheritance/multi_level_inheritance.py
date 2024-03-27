class Person:
    country = "India"
    def takeBreath(self):
        print("I'm breathing..")

class Employee:
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an employee so I am breathing..")
    

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary for Programmers")
    
    def takeBreath(self):
        print("I am an employee so I am breathing++..")   
        
p = Person()
p.takeBreath()
# p.company() #throws an error
e = Employee()
e.takeBreath()
print(e.company)
pr = Programmer()
pr.takeBreath()
print(pr.company)
