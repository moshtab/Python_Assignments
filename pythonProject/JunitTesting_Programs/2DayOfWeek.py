'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Day of a week”
'''

m=int(input("Enter the value of month(1-12)"))
d=int(input("Enter the value of date(1-31)"))
y=int(input(("Enter the year")))
y0 = y - (14 - m) / 12
x = y0 + y0 / 4 - y0 / 100 + y0 / 400
m0 = m + 12 * ((14 - m) / 12) - 2
d0 = int((d + x + 31 * m0 / 12) % 7)
if(d0==0):
    print("Sunday")
elif(d0==1):
    print("Monday")
elif(d0==2):
    print("Tuesday")
elif(d0==3):
    print("Wednesday")
elif(d0==4):
    print("Thursday")
elif(d0==5):
    print("Friday")
elif(d0==6):
    print("Saturday")
else:
    print("Invalid day")

