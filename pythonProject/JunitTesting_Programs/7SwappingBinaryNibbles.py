'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Decimal To Binary and swapping the nibbles and finding decimal value”
'''
from threading import Thread


def decimaltoBinary():
    decimalNum = int(input("Enter a decimal number"))
    if(decimalNum>=1):
        decimaltoBinary(decimalNum//2)
    print(decimalNum%2,end="")

def swapNibbles():
    decimalNum = int(input("Enter a decimal number"))
    print ((decimalNum & 0x0F) << 4 | (decimalNum & 0xF0) >> 4)
def errorhandler():
    print("Invalid choice")
print('''
   1. Decimal To Binary
   2. Swap nibbles and get decimal value
''')
choice=int(input("Enter your choice"))
operations={
    1: decimaltoBinary,
    2: swapNibbles
}
output=operations.get(choice,errorhandler)()
print(output)



