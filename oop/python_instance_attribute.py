# python class attribute is accessible for all. instance attribute only accesible for a instance or object

class Shop:
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]
    def add_to_cart(self,item):
        self.cart.append(item)

abir = Shop("abir")
arif = Shop("arif")
rubel = Shop("rubel")
abir.add_to_cart("mobile")
abir.add_to_cart("watch")
abir.add_to_cart("bike")

arif.add_to_cart("t-shirt")
arif.add_to_cart("pant")
arif.add_to_cart("chocolet")

rubel.add_to_cart("shari")
rubel.add_to_cart("panjabi")
rubel.add_to_cart("lungi")

print(abir.cart)
print(arif.cart)
print(rubel.cart)