file = open("input.txt", "r")
count = 0
prev = int(file.readline())

for line in file:
    if int(line) > prev:
        count += 1
    prev = int(line)

print(count)
