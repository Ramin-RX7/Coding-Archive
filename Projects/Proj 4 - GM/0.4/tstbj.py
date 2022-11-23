'''
Dice Game
author: Bogdanov Bogdan
'''

from random import randrange

#----------Function print_dice----------------------------
def print_dice(dice_one, dice_two):
    
    #---------Lists for the formation of the dice----------
    d1 = ['422222224',
          '300000003',
          '300010003',
          '300000003',
          '422222224']

    d2 = ['422222224',
          '301000003',
          '300000003',
          '300000103',
          '422222224']
    
    d3 = ['422222224',
          '300000103',
          '300010003',
          '301000003',
          '422222224']
        
    d4 = ['422222224',
          '301000103',
          '300000003',
          '301000103',
          '422222224']
        
    d5 = ['422222224',
          '301000103',
          '300010003',
          '301000103',
          '422222224']      
    
    d6 = ['422222224',
          '301000103',
          '301000103',
          '301000103',
          '422222224']
          
    dice = [d1, d2, d3, d4, d5, d6]
    #--END----Lists for the formation of the dice------
    
    
    d1 = dice[dice_one-1]
    d2 = dice[dice_two-1]
    res_dice = []
    
    #-----------combine dice--------
    for i in range(0,5):
        res_dice.append(d1[i]+d2[i])
        i += 1
    #---END-----combine dice-------    
    
    #----------Print two dice------
    i = 0      
    res = ''      
    for ls in res_dice:
        for t in ls:
            if i == len(ls)/2: res += '   '
            if t =='2':
                res += '-'
            elif t == '3':
                res += '|'
            elif t == '4':
                res += '+'
            elif t == '1':
                res += 'O'
            else:
                res += ' '
            i += 1    
        print(res)
        res = ''
        i = 0
    #---END----Print two dice------
#--END-----Function print_dice------------------

#------Your roll two dice, and their sum--------
player_dice_one = randrange(1,6)               
player_dice_two = randrange(1,6)
player_scope = player_dice_one + player_dice_two 

#------Your roll two dice, and their sum--------
comp_dice_one = randrange(1,6)
comp_dice_two = randrange(1,6)
comp_scope = comp_dice_one + comp_dice_two 

#---------Determine the winner------------------
if player_scope > comp_scope:
    print('-------You Win-------')
elif player_scope < comp_scope:
    print('------You Lose...----')
else:
    print('--------Draw---------')
#---END---Determine the winner------------------

#---------Print result--------------------------
print(u'\u0020'*7+str(player_scope)+' Vs '+str(comp_scope))
print('\n......your roll......')    
print_dice(player_dice_one, player_dice_two)
print('\n......comp roll......')
print_dice(comp_dice_one, comp_dice_two)
print('press run that would \n     play again'.upper())
print("\n Please leave a like \n   if you enjoyed!")
        
import time
time.sleep(10)