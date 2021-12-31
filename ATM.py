class Atm(object):
    def __init__(self, userName, password, balance):
        self.userName= userName
        self.password = password
        self.balance = balance

    def atmName(self):
        print("abc")

    def cashWithdrawl (self):
        print("Done")

bank = Atm("Yash", "abc123456", "5,000" )
print(bank.userName)
print(bank.password)
print(bank.balance)


     