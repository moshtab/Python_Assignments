'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Windchill”
'''
import math
import sys
def windchill(t,v):
    w = 35.74 + (t * 0.615) + (0.4275 * t - 35.75) * (math.pow(v, 0.16))
    print("WIndchill is :",w)
t=int(input("Enter a value of t(0-50) :"))
if(t>50):
    sys.exit()
v=int(input("Enter a value of v(3-120) :"))
if(v<3 and v>120):
    sys.exit()
windchill(t,v)