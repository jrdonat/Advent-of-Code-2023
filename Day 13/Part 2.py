#! WIP - UNCLEAR INSTRUCTIONS !#

from itertools import pairwise
def check(block: list[str], data: tuple[int,int]) -> bool:
    tolerance = 0 if data[1] == -2 else 1
    if data[1] != -2:
        pass
    iter = data[0] + 0.5
    counter = 0.5
    while True:
        try:
            if block[int(iter - counter)] == block[int(iter + counter)]:
                counter += 1
            elif iter-counter < 0: 
                return True
            else:
                return False
        except IndexError:
            return True

def lineCheck(line1: str, line2: str) -> int:
    tolerance = -2
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            tolerance = i
            if tolerance >= 0:
                return -1
    return tolerance


with open('Day 13\\input.txt') as file:
    input = file.read().split('\n\n')
    runningSum = 0
    for block in input:
        horizontalMatches = []
        for line1, line2 in pairwise(enumerate(block.split('\n'))):
            if lineCheck(line1[1], line2[1]) != -1:
                horizontalMatches.append((line1[0],lineCheck(line1[1], line2[1])))
        for match in horizontalMatches:
            if check(block.split('\n'), match):
                runningSum += 100*(match+1)
        block = list(zip(*block.split('\n')[::-1]))
        block = [''.join(x) for x in block]
        verticalMatches = []
        for line1, line2 in pairwise(enumerate(block)):
            if line1[1] == line2[1]:
                verticalMatches.append(line1[0])
        for match in verticalMatches:
            if check(block, match):
                runningSum += match+1
    print(runningSum)
