infile = open('test-1.txt', 'r')

right = 3
down = 0
counter = 0

for line in infile:
    if not down:
        down += 1
        continue
    if line[:-1][right % len(line[:-1])] == '#':
        counter += 1
    right += 3
    down += 1
    
print(counter)
