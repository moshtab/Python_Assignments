'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Prime Numbers”
'''
def primeNumber(lower_value, upper_value):
    for num in range(lower_value,upper_value+1):
        if(num>1):
            flag = 0
            for i in range(2, num):
                if (num % i == 0):
                    flag = 1
                    break
            if (flag == 0 and num != 1):
                print(num, end=' ')
lower_value=int(input("enter the lower value"))
upper_value=int(input("enter the upper value"))
primeNumber(lower_value,upper_value)