from copy import deepcopy

# Beginning stage of Chopsticks
def add_next_number(total,n):
    total = total + n
    return total

def sum_all_numbers(m):
    total = 0
    for i in range(1,m+1):
        total = add_next_number(total,i)
    print(total)

sum_all_numbers(100)

player1 = {'left':4, 'right':1}
player2 = {'left':1, 'right':1}


# Possible Moves
def combine(player1):
    left = player1['left']
    right = player2['right']
    difference = abs(right - left)
    maximum = left+right
    # from left hand to right hand
    for i in range():




def strike(player1, player2):
    for myhand in ['left','right']:
        for theirhand in ['left','right']:
            temp_player = deepcopy(player2)
            if player1[myhand] == 0:
                pass#no move!
            elif temp_player[theirhand] == 0:
                pass#no move!
            else:
                temp_player[theirhand] = player1[myhand] + temp_player[theirhand]
                if temp_player[theirhand] >= 5:
                    temp_player[theirhand] = 0
            print(player1, player2, temp_player)


print(strike(player1,player2))