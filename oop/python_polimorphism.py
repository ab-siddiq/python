class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def designation(self):
        return "Production"
class Admin(Employee):
    def designation(self):
        return "Executive"
class Development(Employee):
    def designation(self):
        return "Programmer"
class Management(Employee):
    def designation(self):
        return "Manager"
class Legal(Employee):
    def designation(self):
        return "Adviser"
admin = Admin("Raihan",2233)
dev = Development("Jahid",2293)
mang = Management("Shams",3233)
leg = Legal("Musfiq",2213)
for x in (admin,dev,mang,leg):
    print(x.name,"is a",x.designation())
