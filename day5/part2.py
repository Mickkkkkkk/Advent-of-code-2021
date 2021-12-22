"""
kunne brukt range x1 -> x2, y1 -> y2 bare
"""

from collections import defaultdict

vent_coordinates = defaultdict(lambda:0)

with open("input.txt") as file:
    i = 0
    for line in file:
        xyxy = [int(num) for a in line.split(" -> ") for num in a.split(",")]
        xy = (xyxy[0], xyxy[1])
        additions = [(xy[0]-xyxy[2] > 0 and -1) or (xy[0]-xyxy[2] < 0 and 1) or 0, (xy[1]-xyxy[3] > 0 and -1) or (xy[1]-xyxy[3] < 0 and 1) or 0]
        assert abs(xy[0]-xyxy[2]) == abs(xy[1]-xyxy[3]) or (xy[0] == xyxy[2] or xy[1] == xyxy[3])
        while xy[0] != xyxy[2] or xy[1] != xyxy[3]:
            vent_coordinates[xy] += 1
            xy = (xy[0]+additions[0], xy[1]+additions[1])
        vent_coordinates[(xyxy[2], xyxy[3])] += 1
        i += 1

print(sum([1 for x in vent_coordinates.values() if x > 1]))
