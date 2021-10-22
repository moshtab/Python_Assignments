'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Prime Numbers in range (0-1000)
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
                return (num)
    
def anagram(a):
    anagram_list=[]
    for i in range(a):
        for j in range(a):
            if i!=j and (sorted(str(i))==sorted(str(j))):
                anagram_list.append(i)
    return anagram_list
if __name__ == '__main__':
    lower_value = int(input("enter the lower value"))
    upper_value = int(input("enter the upper value"))
    a=primeNumber(lower_value, upper_value)
    print(a)
    anagram(a)
    print(anagram(a))



