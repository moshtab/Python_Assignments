'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Harmonic Number”
'''
def harmonicNumber(num):
    sum=0
    for i in range(1,num+1):
        sum = sum +1/i
    print("Harmonic number is :",sum)
num = int(input("Enter a number"))
harmonicNumber(num)