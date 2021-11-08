#Create a program that will ask how many apples and oranges you want to buy.
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
#Display the output in the following format.
#The total amount is ______.

def ShowScene():
    print("You are 8 members in the family. You are asked by your mother to buy some fruits in the market for maintaining healthy lifestyle because it can help all the members of the family to boost your immunity especially in this time of pandemic. When you got in the market, you saw the prices of the fruits.")

def AmountFruits():
    _amountApple = int(input("Enter the price of the Apple in the market: "))
    _amountOrange = int(input("Enter the price of the Orange in the market: "))
    return _amountApple, _amountOrange

def NumberFruits():
    _numberApple = int(input("Miss, how many apples do you want to buy? "))
    _numberOrange = int(input("And how many oranges do you want to buy? "))
    return _numberApple, _numberOrange

def ShowScene2():
    print("Since, you have seen that the price of Apple is 20 pesos, and the price of an Orange is 25 pesos each, you will now calculate the total amount you will be paying.")

def PayFruits(_amountApple, _amountOrange, _numberApple,  _numberOrange):
    _payApple = int(_amountApple*_numberApple)
    _payOrange = int(_amountOrange*_numberOrange)
    return _payApple, _payOrange

def FullAmount(_payApple, _payOrange):
    _fullAmount = int(_payApple + _payOrange)
    return _fullAmount

def DisplayTotal(_fullAmount):
    print(f"The total amount is {_fullAmount}.")

# Steps
# put a situation
Set = ShowScene()
# 1. display the price of apple and orange
PriceA, PriceO = AmountFruits()
# 2. ask the number of apples and oranges to buy
Apple, Orange = NumberFruits()
# put another situation
Set2 = ShowScene2()
# 3. compute the amount by multiplying the number of fruits to its price
TotalApple, TotalOrange = PayFruits(PriceA, PriceO, Apple, Orange )
# 4. display the total amount to pay for all the fruits to be bought
TotalFruits = FullAmount(TotalApple, TotalOrange)
# 5. display the statement
FinalStatement = DisplayTotal(TotalFruits)