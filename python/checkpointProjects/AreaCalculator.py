# Area calculator
import math
print('==================\nArea Calculator 📐\n==================')

quit = False

while not quit:
    try:
        selection = int(input('For which shape do you want to calculate the area? \n 1) Square \n 2) Rectangle \n 3) Triangle \n 4) Circle \n 5) Quit \n Your choice: '))

        # Square
        if selection == 1: 
            side = int(input('What is the length of the sides: '))
            area = side ** 2
            print('The area is ', area, '\n')    
        # Rectangle
        elif selection == 2:
            length = int(input('What is the length of the rectangle: '))
            width = int(input('What is the width of the rectangle: '))
            area = length * width
            print('The area is ', area, '\n')

        # Triangle
        elif selection == 3:
            height = int(input('What is the height of the triangle: '))
            base = int(input('What is the base of the triangle: '))
            area = (height * base) / 2
            print('The area is ', area, '\n')

        # Circle
        elif selection == 4:    
            radius = int(input('What is the radius of the circle: '))
            area = math.pi * radius **2
            print('The area is ', area, '\n')

        elif selection == 5:
            quit = True
            print('Goodbye')

        else:
            raise ValueError('Incorrect selection. Please select a value from 1 to 5.')
        
    except ValueError as e:
        print(f'Error: {e}\n')

    

