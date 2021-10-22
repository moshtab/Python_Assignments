'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Power of 2.”
'''
def powersOf2():
    power = int(input("Enter the power of 2"))
    answer =1
    for i in range(power):
        answer=answer*2

    print("Answer is :",answer)
powersOf2()

