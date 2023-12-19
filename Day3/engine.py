
file = open('Day3\\input.txt')
lines = file.readlines()

for i, line in enumerate(lines):
    for j, n in enumerate(line):
        if(n.isdigit()):
            left = False; right = False; above = False; below = False
            topLeft = False; topRight = False; bottomLeft = False; bottomRight = False
            if(j > 0 and j < len(line)):
                left = (not line[j + 1].isdigit()) and line[j + 1] != '.'
                right = (not line[j - 1].isdigit()) and line[j - 1] != '.'
            if(i > 0 and i < len(lines)):
                above = (not lines[i + 1][j].isdigit()) and lines[i + 1][j] != '.'
                below = (not lines[i - 1][j].isdigit()) and lines[i - 1][j] != '.'
        if(left or right or above or below):
            pass