# python class method need a self parameter otherwis it will through an error. If we declare muliple parametre and forgot to add self then it will take the first parameter as self
class Calculator:
    
    def sum(self,num1,num2):
        return num1+num2
c=Calculator()
print(c.sum(3,5))