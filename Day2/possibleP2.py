file = open('Day2\\input.txt')
lines = file.readlines()

power_sum = 0

for line in lines:
    min_red = 0
    min_green = 0
    min_blue = 0
    game = line.split('Game ')[1].split(':')
    id = game[0]
    hands = game[1].split(';')
    possible = True
    for hand in hands:
        sets = hand.split(',')
        for cubes in sets:
            if(cubes.find('red') >= 0 and int(cubes.split('red')[0]) > min_red):
                min_red = int(cubes.split('red')[0])
            if(cubes.find('green') >= 0 and int(cubes.split('green')[0]) > min_green):
                min_green = int(cubes.split('green')[0])
            if(cubes.find('blue') >= 0 and int(cubes.split('blue')[0]) > min_blue):
                min_blue = int(cubes.split('blue')[0])
    power_sum += (min_red * min_green * min_blue)
print(power_sum)