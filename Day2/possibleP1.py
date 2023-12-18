file = open('Day2\\input.txt')
lines = file.readlines()

max_red = 12
max_green = 13
max_blue = 14
id_sum = 0

for line in lines:
    game = line.split('Game ')[1].split(':')
    id = game[0]
    hands = game[1].split(';')
    possible = True
    for hand in hands:
        sets = hand.split(',')
        for cubes in sets:
            if(cubes.find('red') >= 0 and int(cubes.split('red')[0]) > max_red):
                possible = False
            if(cubes.find('green') >= 0 and int(cubes.split('green')[0]) > max_green):
                possible = False
            if(cubes.find('blue') >= 0 and int(cubes.split('blue')[0]) > max_blue):
                possible = False
    if possible:
        id_sum += int(id)
print(id_sum)