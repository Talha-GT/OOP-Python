
# class shop:
#     cart=[] #class attribute
#     def __init__(self,buyer):
#         self.buyer=buyer
#     def add_to_cart(self,item):
#         self.cart.append(item)
# mehjabin=shop('meh jabin')
# mehjabin.add_to_cart('Phone')
# mehjabin.add_to_cart('showes')
# print(mehjabin.cart)

# Niso=shop('niso')
# Niso.add_to_cart('Bag')
# Niso.add_to_cart('lal showes')
# print(Niso.cart)




class shop:

    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[] #instance attribute its one kind of variable scope
    def add_to_cart(self,item):
        self.cart.append(item)

mehjabin=shop('meh jabin')
mehjabin.add_to_cart('Phone')
mehjabin.add_to_cart('showes')
print(mehjabin.cart)

Niso=shop('niso')
Niso.add_to_cart('Bag')
Niso.add_to_cart('lal showes')
print(Niso.cart)