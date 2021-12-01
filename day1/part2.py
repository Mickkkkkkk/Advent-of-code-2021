file = open("input.txt", "r")
count = 0
list = [int(x) for x in file]
prev = sum(list[:3])
for i in range(1, len(list)-2):
    if sum(list[i:i+3]) > prev:
        count += 1
    prev = sum(list[i:i+3])


print(count)
