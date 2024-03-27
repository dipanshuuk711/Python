class Employee:
    company = "Google"
    #sometimes we need a function that dosesn't use the
    #self parameter.We can define a static method like this.
    @staticmethod
    def greet():
        print("Good Evening Brother! ") 
    def getSalary(self):
        print("Salary is 100k")
     
dipanshu = Employee()
dipanshu.greet()  
dipanshu.getSalary()
