x = 0
y = 0
aim = 0

for line in open("input.txt"):
    line = line.split(" ")
    if line[0] == "forward":
        x += int(line[1])
        y += int(line[1])*aim
    elif line[0] == "up":
        aim -= int(line[1])
    else:
        aim += int(line[1])

print(x*y)
