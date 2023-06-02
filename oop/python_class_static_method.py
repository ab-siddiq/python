class Calculation:
    @classmethod
    def sum(cls,a,b):
        return a+b
    @staticmethod
    def res(result):
        if(result>10):
            print("Out of budget")
        else:
            print("Within budget")
cal = Calculation()
print(cal.sum(3,5))
cal.res(10)