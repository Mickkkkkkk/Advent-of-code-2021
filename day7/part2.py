"""
from collections import Counter

crabs = Counter([int(num) for num in open("input.txt").read().split(",")])
min = min(crabs)
max = max(crabs)
lowest_total_fuel = float('inf')

for i in range(min, max):
    fuel_for_i = sum([sum(range(abs(i-pos)+1))*amount for pos, amount in crabs.items()])
    if fuel_for_i < lowest_total_fuel:
        lowest_total_fuel = fuel_for_i

print(lowest_total_fuel)
"""


"""
vet egentlig ikke hvorfor dette virker :/
"""
crabs = [int(num) for num in open("input.txt").read().split(",")]
avg = int(sum(crabs)/len(crabs))
print(sum([sum(range(abs(avg-crab)+1)) for crab in crabs]))
