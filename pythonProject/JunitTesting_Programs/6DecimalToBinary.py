'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Decimal To Binary”
'''
def decimaltoBinary(decimalNum):
    if(decimalNum>=1):
        decimaltoBinary(decimalNum//2)
    print(decimalNum%2,end="")
decimalNum=int(input("Enter a decimal number"))
decimaltoBinary(decimalNum)
