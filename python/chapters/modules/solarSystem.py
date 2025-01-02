# Write code below 💖

from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planets = ch(planets)

if random_planets == 'Mercury':
    r = 2440
elif random_planets == 'Venus':
    r = 6052
elif random_planets == 'Earth':
    r = 6371
elif random_planets == 'Mars':
    r = 3390
elif random_planets == 'Saturn':
    r = 58232
else:
    print('Oops! An error occurred.')




area = 4 * pi * r**2
print(f'Area of {random_planets} is {round(area,2)} km².')