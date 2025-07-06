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

player1 = {'left':1, 'right':3}
player2 = {'left':0, 'right':2}

def check_if_hand_full(hand):
    if hand >= 5:
        hand = 0
    return hand

def if_winner(player):
    if player['left'] == 0 and player['right']==0:
        #winner
        return True
    else:
        return False

# Possible Moves
def combine(player):
    # from left hand to right hand
    left = player['left']
    right = player['right']
    maximum = max(left,right)
    print(maximum)

    a,b = ['left','right']
    if right > left:
        a,b = ['right','left']

    for i in range(maximum+1):
        temp_player = deepcopy(player)
        temp_player[b] = temp_player[b] + i
        temp_player[b] = check_if_hand_full(temp_player[b])
        temp_player[a] = temp_player[a] - i
        temp_player[a] = check_if_hand_full(temp_player[a])
        print(temp_player)

combine(player1)


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
                temp_player[theirhand] = check_if_hand_full(temp_player[theirhand])
            print(player1, player2, temp_player,if_winner(temp_player))


print(strike(player1,player2))