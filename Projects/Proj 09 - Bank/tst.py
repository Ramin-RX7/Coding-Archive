# import Bank
from Bank import *

Bank.RegisterName.__Banks = {'g':'sdaf'}
b1 = RegisterBank(name='bank1')
#print(Bank.Bank.RegisterName.__Banks)
#print(b1.Get_Banks())
#print(Bank.Bank.RegisterName.__Banks)
b2 = RegisterBank(name='bank2')
#print(b2.Get_Banks())


a1 = Account('acc1')
a1.transact('','','','bank1')



