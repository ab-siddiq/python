class Calculation:
    def __init__(self,a,b,c) -> None:
        self.a=a
        self.b=b
        self.c=c
    def sum(self):
        print(self.a+self.b+self.c)
    def factorial(self):
        fac=1
        for i in range (2,self.b+1):
            fac*=i
        print(fac)
cal = Calculation(1,5,3)
cal.sum()
cal.factorial()