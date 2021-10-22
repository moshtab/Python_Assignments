'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Monthly Payment”
'''
import math
def monthlyPayment(P,Y,R):
    n = 12 * Y
    r = R / 1200
    payment = (P * r) / (1 - math.pow((1 + r), -n))
    print("Monthly Payment is :",payment)
P=int(input("Enter the Principle amount :"))
Y=int(input("Enter the number of years :"))
R= int(input("Enter the rate of intrest :"))
monthlyPayment(P, Y, R)