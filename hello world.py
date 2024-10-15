import random

def hit_chance_pvp():
    player_name = input("Enter your name, player: ")
    player2_name = input("Enter your name, player2: ")
    player_hp = 50
    opponent_hp = 50

    while True:
        print(f"\n{player_name}'s turn!")

        while True:
            player_hit_power = int(input(f'{player_name}, choose your hit power from one to nine: '))
            if player_hit_power > 9 or player_hit_power < 1:
                print('Sorry, you should only choose numbers from 1 to 9! Try again.')
            else:
                break
        player_chance = random.randint(1, 6)
        player_chance_to_miss = player_hit_power - player_chance

        if player_chance_to_miss > 0:
            opponent_hp -= player_chance_to_miss
            print(f'{player_name} hits {player2_name} by {player_chance_to_miss} !')
            print(f'{player2_name} now has {opponent_hp} HP left.')
        else:
            print(f'{player_name} missed!')


        if opponent_hp <= 0:
            print(f'{player2_name} is defeated!')
            break

        print(f"\n{player2_name}'s turn!")
        while True:
            opponent_hit_power = int(input(f'{player2_name}, choose your hit power from one to nine: '))
            if opponent_hit_power > 9 or opponent_hit_power < 1:
                print('Sorry, choose only numbers from 1 to 9! Try again.')
            else:
                break

        opponent_chance = random.randint(1, 6)
        opponent_chance_to_miss = opponent_hit_power - opponent_chance

        if opponent_chance_to_miss > 0:
            player_hp -= opponent_chance_to_miss
            print(f'{player2_name} hits {player_name} by {opponent_chance_to_miss} points!')
            print(f'{player_name} has {player_hp} HP left.')
        else:
            print(f'{player2_name} missed!')
        if player_hp <= 0:
            print(f'{player_name} is defeated! {player2_name} wins!')
            break

def hit_chance_PvE():
    player_name = input("Enter your name, player: ")
    bot_name = "Bot"
    player_hp = 50
    bot_hp = 50

    while True:
        print(f"{player_name}'s turn!")
        while True:
            player_hit_power = int(input(f'{player_name}, choose your hit power from one to nine: '))
            if player_hit_power > 9 or player_hit_power < 1:
                print('Sorry, choose only numbers from 1 to 9! Try again.')
            else:
                break

        player_chance = random.randint(1, 6)
        player_chance_to_miss = player_hit_power - player_chance

        if player_chance_to_miss > 0:
            bot_hp -= player_chance_to_miss
            print(f'{player_name} hits {bot_name} and reduces their HP by {player_chance_to_miss} points!')
            print(f'{bot_name} now has {bot_hp} HP left.')
        else:
            print(f'Sorry, {player_name}, you missed!')

        if bot_hp <= 0:
            print(f'{bot_name} is defeated! {player_name} wins!')
            break


        print(f"\n{bot_name}'s turn!")
        bot_hit_power = random.randint(1, 9)
        print(f'{bot_name} chooses a hit power of {bot_hit_power}.')

        bot_chance = random.randint(1, 6)
        bot_chance_to_miss = bot_hit_power - bot_chance

        if bot_chance_to_miss > 0:
            player_hp -= bot_chance_to_miss
            print(f'{bot_name} hits {player_name} and reduces their HP by {bot_chance_to_miss} points!')
            print(f'{player_name} now has {player_hp} HP left.')
        else:
            print(f'{bot_name} missed!')

        if player_hp <= 0:
            print(f'{player_name} is defeated! {bot_name} wins!')
            break

print("Hello welcome aboard! ")
game_mood = input(''''\nplease choose your game mood: 
-pvp
-pve
-quit
''')
while True:
    if game_mood == 'pvp':
        hit_chance_pvp()
    elif game_mood == 'pve':
        hit_chance_PvE()
    elif game_mood == 'quit':
        break
    else:
        print('soryy I didn\'t understand!!!')
        print("Please choose your game mood:")
