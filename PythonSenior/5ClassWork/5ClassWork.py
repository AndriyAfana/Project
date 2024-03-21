from Character import Character
from Berserk import Berserk
from Vampyre import Vampyre
import time


player1 = Berserk('Vasya', damage=15)
player1.show_info()

player2 = Vampyre('Petya', damage=10)
print(player2)

while player1.is_alive() and player2.is_alive():
      vampiric_damage = player2.damage / 100 * 10
      time.sleep(2.000)

      p1_damage = player1.attack(player2)
      print(f'{player1.name} атакував {player2.name} '
            f'і наніс {p1_damage} шкоди.')

      p2_damage = player2.attack(player1)
      print(f'{player2.name} атакував {player1.name} '
            f'і наніс {p2_damage} шкоди' f', і відновив {vampiric_damage} HP')

      print(player1, player2, sep='\n')

print(player1, player2, sep='\n')