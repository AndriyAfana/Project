from Character import Character
import time

player1 = Character('cmetankaicalo', damage=50, health=100)
player1.show_info()


player2 = Character('caloiborch', damage=25, health=100)
print(player2)

while player1.is_alive() and player2.is_alive():
      time.sleep(2.000)
      p1_damage = player1.attack (player2)
      print(f'{player1.name} aтakував {player2.name} '
            f'i нанic {p1_damage} шкоди.')
      p2_damage = player2.attack (player1)
      print(f'{player2.name} aтакував {player1.name} ' 
            f'1 наніс {p2_damage} шкоди.')
      print(player1, player2, sep='\n')



