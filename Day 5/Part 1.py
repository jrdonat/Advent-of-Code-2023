import re
#* I try to make these so that it'd work with any input and not just the specific one *#
section = 1
sections = []

"""
Section 1: Seeds -> Is not added to sections table
Section 2: Seeds-to-soil
Section 3: Soil-to-fertilizer
Section 4: Fertilizer-to-water
Section 5: Water-to-light
Section 6: Light-to-temperature
Section 7: Temperature-to-humidity
Section 8: Humidity-to-location
"""


def checkForSourceRange(seed: int, section: int) -> int:
    for set in sections[section-2]:
        if (set[1]+set[2]) >= seed > set[1]:
            return seed - set[1] + set[0]
    return seed

with open("Day 5\\input.txt","r") as file:
    lines = file.read().split("\n")
    seeds = list(map(int,lines[0][7:].split(" ")))
    last = False
    for line in lines:
        if re.search(r"^\d", line) and not last:
            section += 1
            last = True
            sections.append([])
            sections[section-2].append(list(map(int,line.split(" "))))
        elif re.search(r"^\d", line) and last:
            last = True
            sections[section-2].append(list(map(int,line.split(" "))))
        else:
            last = False
            continue
    for i in range(2,9):
        seeds = list(map(checkForSourceRange, seeds, [i]*len(seeds)))
    print(sorted(seeds)[0])
