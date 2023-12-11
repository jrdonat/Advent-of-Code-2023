from itertools import combinations
with open("Day 11\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    insertVals = []
    for i, line in enumerate(input):
        if line.count(line[0]) == len(line):
            insertVals.append(i)
    for j, i in enumerate(insertVals):
        input.insert(i+j,"."*len(input[0]))
    input = list(zip(*input[::-1]))
    insertVals.clear()
    for i, line in enumerate(input):
        if line.count(line[0]) == len(line):
            insertVals.append(i)
    for j, i in enumerate(insertVals):
        input.insert(i+j,"."*len(input[0]))
    coords = []
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "#":
                coords.append((x,y))
    runningSum = 0
    for coord1, coord2 in combinations(coords, 2):
        dist = abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])
        runningSum += dist
    print(runningSum)