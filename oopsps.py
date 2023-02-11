class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name =  name
        self.product = product

    def getInfo(self):
        print(f"The name of the employee is {self.name}")
        print(f"The product of the employee is {self.product}")

sahil = Programmer("Sahil","Skype")
neha = Programmer("Neha","Github")
sahil.getInfo()
neha.getInfo()