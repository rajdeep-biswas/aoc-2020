infile = open('input-1.txt', 'r')

totalcount = 0

for line in infile:
    splitline = line.split()
    [occurdn, occurup] = splitline[0].split('-')
    letter = splitline[1][0]
    string = splitline[2]

    if (string[int(occurdn) - 1] == letter) ^ (string[int(occurup) - 1] == letter):
        totalcount += 1
    # print(occurup, occurdn, letter, string)
    # print(line.split())

print(totalcount)
