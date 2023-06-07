class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class B(A):
    print("Calling from class B")

b = B("Abu Bakkar",28)
print(b.age,b.name)