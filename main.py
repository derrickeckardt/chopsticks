# Beginning stage of Chopsticks
player1 = [1, 1]
player2 = [1, 1]

# min = [0, 1]
# max = [4, 4]


# Possible Moves
def combine(player1, player2):
    pass

def strike(player1, player2):
    pass

def add_next_number(total,n):
    total = total + n
    print(total)
    return total

def sum_all_numbers(m):
    total = 0
    for i in range(1,m+1):
        total = add_next_number(total,i)

sum_all_numbers(100)