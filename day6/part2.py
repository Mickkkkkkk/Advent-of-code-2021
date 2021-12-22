timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for fish in open("input.txt").read().split(","):
    timers[int(fish)] += 1
day = 0
while day < 256:
    prev_timer = 0
    for i in range(8, -1, -1):
        if i == 0:
            timers[6] += timers[i]
            timers[8] = timers[i]
            timers[i] = prev_timer
        else:
            new_prev = timers[i]
            timers[i] = prev_timer
            prev_timer = new_prev
    day += 1

print(sum(timers))
