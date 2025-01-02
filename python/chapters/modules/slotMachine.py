# Write code below 💖

import random

slots = ['🍒',' 🍇', '🍉', '7️⃣']
play = True

def play():
  results = random.choices(slots,k=3)

  print('\n',results[0], ' |', results[1], ' |', results[2])

  if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
    print('Jackpot! 💰\n')
  else:
    print('Thanks for playing!\n')

while play:
  play()
  keepPlaying = input('Do you want to play again (Y / N)? ')
  if keepPlaying in ['n','N']:
    play = False
    print('Thanks for playing!')


