file = open("input.txt")

gamma = [int(x) for x in file.readline() if x!= "\n"]
print(len(gamma))

for line in file:
    print(len(line))
    for i in range(len(line)-1):
        gamma[i] += (line[i] == "0" and -1) or 1

gamma = [0 if x < 0 else 1 for x in gamma]
epsilon = [0 if x == 1 else 1 for x in gamma]

gam = 0
eps = 0
for g,e in zip(gamma, epsilon):
    gam = (gam << 1) | g
    eps = (eps << 1) | e

print(gam*eps)
