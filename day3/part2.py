file = open("input.txt")

o2_binaries = [[int(s) for s in line if s != "\n"] for line in file]
co2_binaries = o2_binaries
bit_len = len(o2_binaries[0])

i = 0
while i < bit_len:
    if len(o2_binaries) > 1:
        o2_new = []
        o2_counter = 0
        for bits in o2_binaries:
            o2_counter += (bits[i] == 0 and -1) or 1
        o2_counter = (o2_counter >= 0 and 1) or 0 # IKKE BRA, 0 er FALSE
        for bits in o2_binaries:
            if bits[i] == o2_counter:
                o2_new.append(bits)

    # FIKK ERROR UTEN DENNE, ALTSÅ HVIS BARE 1 FØR
    # i>bit_len SÅ FJERNA DEN SISTE. SKAL IKKE SKJE?
    # FORDI HVIS 1, VIL LEAST COMMON VÆRE 0, MEN INGEN
    # ER 0, FORDI BARE EN BITSTRENG.
    if len(co2_binaries) > 1:
        co2_new = []
        co2_counter = 0
        for bits in co2_binaries:
            co2_counter += (bits[i] == 0 and -1) or 1
        co2_counter = (co2_counter < 0 and 1) or 0 
        for bits in co2_binaries:
            if bits[i] == co2_counter:
                co2_new.append(bits)

    i+=1
    o2_binaries = o2_new
    co2_binaries = co2_new

o2 = 0
co2 = 0
print(o2_binaries[0])
print(co2_binaries[0])
for o,c in zip(o2_binaries[0], co2_binaries[0]):
    o2 = (o2 << 1) | o
    co2 = (co2 << 1) | c

print(o2*co2)

file.close()
