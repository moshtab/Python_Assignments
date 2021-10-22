'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Find Euclidean Distance”
'''
import math
def findDistance():
    x = int(input("Enter the x-value :"))
    y = int(input("Enter the y-value :"))
    distance =math.sqrt(math.pow(x,x)+math.pow(y,y))
    print("Euclidean Distance :",distance)
findDistance()
