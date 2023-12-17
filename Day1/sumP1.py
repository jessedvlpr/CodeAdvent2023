file = open('Day1\\input.txt')
lines = file.readlines()
sum = 0
for line in lines:
    s = ''
    for i in line:
        if(i.isdigit()):
            s += i
    sum += int(s[0] + s[-1])
print(sum)