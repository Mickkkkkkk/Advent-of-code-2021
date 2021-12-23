positions = sorted([int(num) for num in open("input.txt").read().split(",")])
median = positions[int(len(positions)/2)]
print(sum([abs(median-x) for x in positions]))
