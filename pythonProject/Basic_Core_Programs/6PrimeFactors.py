'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Prime Factors”
@Description : a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).
'''
def primeFactors(num):
    for i in range(2,num):
        while(num%i==0):
            print(i)
            num=num/i
    if(num>=2):
        print(num)
num=int(input("Enter a number :"))
primeFactors(num)