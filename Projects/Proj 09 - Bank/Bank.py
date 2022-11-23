"""
TODO:

NOTE:
    ? Make transaction class
"""








import rx7 as rx

def rot13(word, **kwargs):
    '''
    Case Sensetive
    Support Numbers and Symbols But Not Work on Them (Under Maintaince)
    '''
    result = ""
    for v in word:
        c = ord(v)
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        result += chr(c)
    return result

class ConfirmationValidator:
    def __init__(self,name,daily_fee,as_pv):
        self.name = name
        self.daily_fee = daily_fee
        self.as_pv = as_pv
    
    @classmethod
    def as_pv(cls,name,daily_fee):
        return cls(name,daily_fee,True)


    def transact(self,block,bank_signiture,bank):
        cheater_bank = False
        sender,recipient,amount,memo = block

        if (sender.credit)<amount:
            cheater_bank=True

        encrypt = rx.Hash.md5
        temp = encrypt(sender.account_number) + encrypt(recipient.account_number) + \
               encrypt(str(amount))           + encrypt(memo)
        hashed = encrypt(temp)

        if hashed != rot13(bank_signiture):
            cheater_bank=True
        
        return (not cheater_bank)


    def confirm_service(self,block,bank_signature,bank):
        self.transact()





PV = ConfirmationValidator.as_pv("MAIN PV",10)
def Get_PV():
    return PV




class Bank:
    class RegisterName:
        __Banks = {}
        def __init__(self,name,self2) -> None:
            if name not in Bank.RegisterName.__Banks:
                Bank.RegisterName.__Banks[name] = self2
            else:
                raise Exception('There is already a bank with this name')
        @staticmethod
        def Get_Banks():
            return Bank.RegisterName.__Banks

    def __init__(self,name,CV=[],Fee=None):
        self.name = name
        self.ConfirmationValidators = CV
        self.cvs = self.ConfirmationValidators
        self.Fee = Fee
        self.NetworkID = None
        self.AccountNumber = None
        Bank.RegisterName(self.name,self)
        self.PrimaryValidator = Get_PV()
        """
        self.signiture
        self.Port = 
        Protocol
        Version
        Node_Type
        """

    def ReadyCheck(self):
        name = self.name
        if not self.ConfirmationValidators:
            raise Exception(f'No CV Found for Bank "{name}"')
        if not self.Fee:
            print(f'[Warning]: Bank "{name}" has no Fee')
        if not self.NetworkID:
            raise Exception(f'No NetworkID found for Bank "{name}"')
        if not self.AccountNumber:
            raise Exception(f'No Account Found for Bank "{name}"')
        return True

    def Get_Banks(self):
        return Bank.RegisterName.Get_Banks()

    def transact(self,block):
        sender,recipient,amount,memo = block
        
        if (sender.credit)<amount:  return False

        encrypt = rx.Hash.md5
        temp = encrypt(sender.account_number) + encrypt(recipient.account_number) + \
               encrypt(str(amount))           + encrypt(memo)
        hashed = encrypt(temp)
        signature = rot13(hashed)
        return signature
        # Get_PV().transact(block,signature,self)


class RegisterBank:
    #? Is it realy needed?
        # reason i did it is: i dont wanna let others access to Bank Class.
    def __new__(cls,*args,**kwargs):
        return Bank(*args,**kwargs)




class Account:
    def __init__(self,Name):
        self.Name = Name
        #self.AccountNumber = 
        #self.SigningKey =
        self.Credit = 0
        #self.credit_key = 
        self.DefaultBank = None
        self.Friends = []

    def transact(self,recipient:"Account",amount:int,memo:str,bank:Bank):
        # bank = Bank.RegisterName.Get_Banks()[bank]
        block = [self,recipient,amount,memo] #should i pass 'self' or 'self.accountnom'?
        Transact.transact(block,bank)
        



class Transact:
    @staticmethod
    def transact(block:list,bank:Bank):
        bank_signature = bank.transact(block)
        if not bank_signature:
            print("Transaction Failed. (In Bank)")
            return
        
        pv_response = Get_PV().transact(block,bank_signature,bank)

        cvs_responses = []
        for cv in bank.ConfirmationValidators:
            cvs_responses.append(cv.confirm_service(block,bank_signature,bank,))
        
        if cvs_responses:pass

        



bnk= RegisterBank(name='BANK1')
acc= Account("Ramin")
acc.Credit = 100
acc2= Account("Ali")


acc.transact(acc2,25,"",bnk)





