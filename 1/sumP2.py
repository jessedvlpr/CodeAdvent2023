numbers =   {
                'one': '1',
                'two': '2', 
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'
            }

file = open('input.txt')
lines = file.readlines()
sum = 0
count = 0
for line in lines:
    count += 1
    s = ''
    for i, n in enumerate(line):
        for f in numbers:
            if(line.find(f) >= 0 and i == line.find(f)):
                line = line[:i] + numbers.get(f) + line[i + 1:]
    for i, n in enumerate(line):
        if(n.isdigit()):
            s += n
    sum += int(s[0] + s[-1])
print(sum)