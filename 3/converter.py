infile = open('input-1.txt', 'r')
outfile = open('test-1.txt', 'w')

string = ''
alph = 'abcdefghijklmnopqrstuvwxyz01234567890' 
count = 0

for line in infile:
    for letter in line:
        if letter == '.':
            string += alph[count % len(alph)]
        else:
            string += letter
        count += 1
        
with outfile as f:
    for line in string:
        f.write(line)
