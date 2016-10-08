import random

def append_random(player):
    player.append(random.randrange(1, 7))

def sorting_dice(player):
    player.sort(reverse=True)
    
def play(player_1, player_2):
    for i in range(3):
        append_random(player_1)
    for i in range(2):
        append_random(player_2)

    sorting_dice(attacker)
    sorting_dice(defender)

def print_result(player_1, player_2):
    print('Dice:')
    print("{}{}{}{}{}" .format(player_1[0],'-', player_1[1], '-', player_1[2]))
    print("{}{}{}" .format(player_2[0],'-', player_2[1]))

attacker = []
defender = []

play(attacker, defender)

print_result(attacker, defender)