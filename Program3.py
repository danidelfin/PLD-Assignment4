#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

def ShowScene():
    print("One day in a market, a daughter named, Chloe, is struggling to know how many apples she can buy with the money she saved, so she aked her mother for help.")

def GetMoneyApple():
    print("Chloe, how much money do you have to buy apples?")
    _getMoney = int(input("Chloe answered her mother: "))
    print("Mother turned to the fruit seller and asked, how much does one apple costs, Miss?")
    _getApple = int(input("Seller answered the mother: "))
    return _getMoney, _getApple

def GetPieces(_getMoney, _getApple):
    _getPieces = int(_getMoney//_getApple)
    return _getPieces

def GetChange(_getMoney, _getApple, _getPieces):
    _getChange = int(_getMoney-(_getApple*_getPieces))
    return _getChange

def DisplayTotalPieces(_getPieces, _getChange):
    print(f"Mother referred to Chloe to say, You can buy {_getPieces} apples and your change is {_getChange} pesos.")
    

#Steps
# put a scenario
Set1 = ShowScene()
# 1. ask for the money on hand and the price of the apple
Money, Apple = GetMoneyApple()
# 2. calculate how many pieces of apple can be bought
PiecesA = GetPieces(Money, Apple)
# 3. compute the change
ChangeA = GetChange(Money, Apple, PiecesA)
# 4. display the statement
FinalStatement = DisplayTotalPieces(PiecesA, ChangeA)

