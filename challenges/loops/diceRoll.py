import random

guess = 0
total = -1

while guess != total:
    guess = int(input('Your guess (2-12): '))
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total =  die1 + die2

print('You got it!') 
