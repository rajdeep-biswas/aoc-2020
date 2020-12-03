infile = open('test-1.txt', 'r')

right = 3
down = 0
counter = 0

for line in infile:
    if not down:
        down += 1
        continue
    linbac = line
    line = line[:-1]
    pos = right % len(line)
    if line[pos] == '#':
        # line = line[:pos] + 'X' + line[pos+1:]
        counter += 1
    # else:
        # line = line[:pos] + 'O' + line[pos+1:]
    
    print(line[pos], 'line ' + str(down), pos)
    right += 3

    """
    # print((line[:-1] * lines)[right], 'line ' + str(down), right)
    if down == 0:
        down += 1
        continue
    right += 3
    pos = right % len(line)
    if line[pos] == '#':
        line = line[:pos] + 'X' + line[pos + 1:]
        counter += 1
    else:
        line = line[:pos] + 'O' + line[pos + 1:]
    # print((line[:-1] * lines)[right], 'line ' + str(down), right)
    """
    down += 1
    # print(line)
    # print(linbac)
    # print()

print(counter)
