
homeWeight = float(input('What is your weight on your home planet (in kg - e.g. 69.5): '))
id = int(input('What is the ID of your home planet: '))

relativeGravity = {1:0.38,2:0.91,3:0.38,4:2.53,5:1.07,6:0.89,7:1.14}



if id < 1 or id > 7: 
    print('Invalid planet number')
else:
    targetWeight = homeWeight * relativeGravity[id]
    print('Your weight on the planet is: ' +str(targetWeight) + ' kg')



