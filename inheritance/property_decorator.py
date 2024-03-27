class Employee:
    company = "Bharat Gas"
    salary = 8500
    salaryBonus = 500
    # totalSalary = 9000
    
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary

e = Employee()
print(e.totalSalary)       
e.totalSalary = 9500
print(e.salary)
print(e.salaryBonus)