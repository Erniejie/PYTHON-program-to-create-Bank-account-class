#program to create Bank account class
#Computer Programming Tutor, 21 Jun 2021

class BankAcct:
    def __init__(self):
        self.bal =0
        print("Banking Application to Accept Deposit and Widthdrawal")
    def deposit(self):
        amt =float(input("Enter Amount to be Deposited: "))
        self.bal +=amt
        print("\nAmount Deposited:",amt)
    def widthdraw(self):
        amt = float(input("Enter Amount to be Widthdrwan: "))
        if self.bal>=amt:
            self.bal-=amt
            print("\nAmount Widthdrawn:",amt)
        else:
            print("\nInsufficient Balance ")
    def showoutput(self):
        print("\nAvailable Balance =",self.bal)

#Creating An Object of Class

bank =BankAcct()
#Calling Functions with that class object
bank.deposit()
bank.widthdraw()
bank.showoutput()
        
