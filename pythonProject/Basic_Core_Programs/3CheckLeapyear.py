'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Print the year is a Leap Year or not.”
'''
def checkLeapYear():
    year = int(input("Enter a year"))
    if((year%100==0) or (year%100!=0) and (year%4==0)):
        print("Given year is Leap Year")
    else:
        print("Given year is not a leap year")
checkLeapYear()
