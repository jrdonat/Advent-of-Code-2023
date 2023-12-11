from itertools import combinations
with open("Day 11\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    crossX = []
    crossY = []
    for i, line in enumerate(input):
        if line.count(line[0]) == len(line):
            crossY.append(i)
    input = list(zip(*input[::-1]))
    for i, line in enumerate(input):
        if line.count(line[0]) == len(line):
            crossX.append(i)
    input = list(zip(*input))[::-1]
    coords = []
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "#":
                coords.append((x,y))
    runningSum = 0
    for coord1, coord2 in combinations(coords, 2):
        multX1 = 0
        multX2 = 0
        multY1 = 0
        multY2 = 0
        for x in crossX:
            if coord1[0] < x < coord2[0]:
                multX2 += 999999
            elif coord2[0] < x < coord1[0]:
                multX1 += 999999
        for y in crossY:
            if coord1[1] < y < coord2[1]:
                multY2 += 999999
            elif coord2[1] < y < coord1[1]:
                multY1 += 999999
        coord1 = (coord1[0]+multX1, coord1[1]+multY1)
        coord2 = (coord2[0]+multX2, coord2[1]+multY2)
        dist = abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])
        runningSum += dist
    print(runningSum)