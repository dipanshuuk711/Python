
class Employee:
    company = "Google"
    
    
    def __init__(self, name, salary, subunit):
        self.name = "Dipanshu"
        self.salary = 10000
        self.subunit = "YouTube"
        print("Employee is created")
    
    def getdetails(self):
        print(f"The name of employee is:  {self.name}")    
        print(f"The salary of employee is: {self.salary}")    
        print(f"The subunit of employee is: {self.subunit}")
            
        
    @staticmethod
    def greet():
        print("Good Evening Brother! ") 
    def getSalary(self):
        print("Salary is 100k")
     

dipanshu = Employee("Dipanshu", 10000, "YouTube")
dipanshu.getdetails()
 