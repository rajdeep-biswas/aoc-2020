infile = open('test-1.txt', 'r')

rightdowns = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
lines = []
product = 1

for line in infile:
    lines.append(line[:-1])

for rightdown in rightdowns:
    right = 0
    down = 0
    counter = 0
    while down < len(lines):
        if not down:
            right += rightdown[0]
            down += rightdown[1]
        if lines[down][right % len(lines[0])] == '#':
            counter += 1
        right += rightdown[0]
        down += rightdown[1]
    product *= counter
    
print(product)
