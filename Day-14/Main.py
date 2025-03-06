import random

import GamePlay

player_1=random.choice(GamePlay.data)
player_2=random.choice(GamePlay.data)
print(player_1)
print(player_2)
def higherLower(gaming1,gaming2):
    if gaming1['Followers Count']>gaming2['Followers Count']:
        print(f'Followers is more for Gamer 1, who is {gaming1['name']}')
    else:
        print(f"Followes is more for Gamer 2 , who is {gaming2['name']}")

higherLower(player_1,player_2)