from collections import defaultdict

vent_coordinates = defaultdict(lambda:0)

with open("input.txt") as file:
    for line in file:
        xyxy = [int(num) for a in line.split(" -> ") for num in a.split(",")]
        if xyxy[0] == xyxy[2]:
            a = min(xyxy[1], xyxy[3])
            while a <= max(xyxy[1], xyxy[3]):
                vent_coordinates[(xyxy[0], a)] += 1
                a += 1
        elif xyxy[1] == xyxy[3]:
            a = min(xyxy[0], xyxy[2])
            while a <= max(xyxy[0], xyxy[2]):
                vent_coordinates[(a, xyxy[1])] += 1
                a += 1

print(sum([1 for x in vent_coordinates.values() if x > 1]))
