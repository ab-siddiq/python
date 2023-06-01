class Employee:
    
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
e1=Employee("abu bakkar","creative developer",20000)
e2=Employee("saiful islam","creative developer",24000)
e3=Employee("rabule ali","creative developer",30000)
print(e1.name,e1.designation,e1.salary)
print(e2.name,e2.designation,e2.salary)
print(e3.name,e3.designation,e3.salary)