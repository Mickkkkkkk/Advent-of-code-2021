x = 0
y = 0

for line in open("input.txt"):
    line = line.split(" ")
    if line[0] == "forward":
        x += int(line[1])
    elif line[0] == "up":
        y -= int(line[1])
    else:
        y += int(line[1])

print(x*y)
