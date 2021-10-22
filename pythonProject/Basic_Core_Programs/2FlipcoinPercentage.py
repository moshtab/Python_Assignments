'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Flip Coin and print percentage of Heads and Tails”
'''
import random
def flipCoinPercentage():
    numOfFlips = int(input("How many times u want to flip the coin"))
    heads = 0
    tails = 0
    tries = 0
    while tries < numOfFlips:
        flip = random.randint(0, 1)
        if flip == 0:
            heads += 1
            tries += 1
        else:
            tails += 1
            tries += 1


    print("Heads won :", (heads / (heads + tails)) * 100 ,"%")
    print("Tails won :", (tails / (tails + heads)) * 100 , "%")
flipCoinPercentage()
