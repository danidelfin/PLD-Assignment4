# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____.

def GetSelfInfo():
    _name = input("What is your name? ")
    _age = int(input("How old are you? "))
    _address = input("Where are you currently residing? ")
    return _name, _age, _address

def DisplaySelfInfo(_name, _age, _address):
    print(f"Hi, my name is {_name}. I am {_age} years old and I live in {_address}.")

# Steps
# 1. ask for name, age, address, and save to variable
Name, Age, Address = GetSelfInfo()
# 2. display name, age, address
Output = DisplaySelfInfo(Name, Age, Address)
