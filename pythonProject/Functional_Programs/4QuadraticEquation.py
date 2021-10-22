'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Find roots of Quadratic Equation”
'''
import math


def quadraticEqnRoots(a,b,c):
    delta = b*b-4*a*c
    if(delta>0):
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Root1 is :", root1)
        print("Root2 is :", root2)
    if(delta==0):
        root1 = -b / (2 * a)
        root2 = -b / (2 * a)
        print("Root1 is :", root1)
        print("Root2 is :", root2)
    if(delta<0):
        print("Roots are imaginary")
a=int(input("Enter a value :"))
b=int(input("Enter b value :"))
c=int(input("Enter c value :"))
quadraticEqnRoots(a,b,c)