#Bob Klemm
#10/23/2025

# Dice Rolling

import math

def d6(total_dice, above_num): #six-sided dice
    #total_dice is number of dice rolled
    #above_num is minimum number needed on each die 
    probability_distribution = []
    
    prob = (7 - above_num) / 6 #probability for one die to be above minimum number 
    
    for i in range(0,total_dice+1): # i is number of dice rolled above minimum number (0 to total dice)
        prob_1 = prob**i * (1-prob)**(total_dice-i)*math.comb(total_dice,i) #calculation
        probability_distribution.append(round(prob_1,4)) #rounds to 4 decimal places
    return probability_distribution #distribution goes from 0 to total dice number

pd = d6(3,3)

print(pd)

def d_n(n, total_dice, above_num): #for non-six-sided-dice, n is number of sides
    #total_dice is number of dice rolled
    #above_num is minimum number needed on each die 
    probability_distribution = []
    
    prob = ((n+1) - above_num) / n #probability for one die to be above minimum number 
    
    for i in range(0,total_dice+1): # i is number of dice rolled above minimum number
        prob_1 = prob**i * (1-prob)**(total_dice-i)*math.comb(total_dice,i) #calculation
        probability_distribution.append(round(prob_1,4)) #rounds to 4 decimal places
    return probability_distribution

pd2 = d_n(8,3,3) #8-sided dice, 3 dice rolled, 3 and up

print(pd2)

#feel free to edit and try some other examples with the functions