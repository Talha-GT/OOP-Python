
class pen:
    def __init__(self,owner,penName,price):
        self.owner=owner
        self.penName=penName
        self.price=price

    def dekhbo(self):
        text=f'pen er nam {self.penName} and er price {self.price}'
        print(text)

mat_ob1=pen('Talha','Matador',10)
mat_ob2=pen('taseen','econo',15)
mat_ob3=pen('maruf','jorina',20)   

print(mat_ob1.owner,mat_ob1.penName,mat_ob1.price)
print(mat_ob2.owner,mat_ob2.penName,mat_ob2.price)
print(mat_ob3.owner,mat_ob3.penName,mat_ob3.price)
mat_ob1.dekhbo()



# class Pen:
#     def __init__(self, owner, penName, price):
#         self.owner = owner
#         self.penName = penName
#         self.price = price

#     def dekhbo(self):
#         text = f'pen er nam {self.penName} and er price {self.price}'
#         print(text)

# mat_ob1 = Pen('Talha', 'Matador', 10)
# mat_ob2 = Pen('Taseen', 'Econo', 15)
# mat_ob3 = Pen('Maruf', 'Jorina', 20)

# print(mat_ob1.owner, mat_ob1.penName, mat_ob1.price)
# print(mat_ob2.owner, mat_ob2.penName, mat_ob2.price)
# print(mat_ob3.owner, mat_ob3.penName, mat_ob3.price)

# mat_ob1.dekhbo()