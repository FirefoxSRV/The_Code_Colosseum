class Change:
    def __init__(self,amount):
        self.amount = amount



amount= int(input("Enter number"))
structure = Change(amount)
changeDenominations = [1,10,25]


coins = 0
while amount :
    if(amount // max(changeDenominations) > 0):
        amount = amount - max(changeDenominations)
        coins +=1
    elif (amount // changeDenominations[1] > 0):
        amount = amount - changeDenominations[1]
        coins +=1
    else:
        amount = amount - changeDenominations[0]
        coins +=1

print(coins)