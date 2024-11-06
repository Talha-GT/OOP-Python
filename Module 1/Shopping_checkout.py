class shopping:
    def __init__(self,GivenMoney):
        self.GivenMoney=GivenMoney
        self.minShop=100
        self.list=[]


    def TotalItem(self,item,pricePerKg,quantity):
         oneObj={'item': item,'pricePerKg':pricePerKg,'quantity':quantity}
         self.list.append(oneObj)

    def checkOut(self):
        print(f'Given money {self.GivenMoney} ')
        total=0
        for item in self.list:
            # print(item)
            total+=item['pricePerKg']*item['quantity']
        # print(total)
        netAmmount=self.GivenMoney-total
        if netAmmount<0:
            print(f"please give us more {abs(netAmmount)} money to cotinue")
        else :
            print(f"Thanks for purchasing product from SRBD and here is your return ammount::{netAmmount}")

         
bigbajar=shopping(1200)
bigbajar.TotalItem('Alu',10,10)
bigbajar.TotalItem('Dal',10,10)
bigbajar.TotalItem('chal',100,10)
bigbajar.checkOut()