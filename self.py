class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary is {self.salary} \n {signature}")
    @staticmethod
    def greet():
        print("Good Morning")


sahil = Employee()
sahil.salary = 100000
sahil.getSalary("Thank you") # Employee.getSalary(sahil)
sahil.greet()
