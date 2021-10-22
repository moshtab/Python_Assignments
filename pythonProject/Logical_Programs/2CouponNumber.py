'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : CouponNumber”
'''
import random
def coupounNumber(cpNum):
    count=0
    for i in range(200):
        randomNum=random.randint(10,100)
        if(randomNum==cpNum):
            count+=1
    print("The Coupon Number ",cpNum," has repeated ",count," times")
cpNum =int(input("Enter a number :"))
coupounNumber(cpNum)


