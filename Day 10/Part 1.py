pipes = {
    "F": ("South", "East"),
    "7": ("South", "West"),
    "J": ("North", "West"),
    "L": ("North", "East"),
    "|": ("North", "South"),
    "-": ("East", "West")
}

directions = {
    "North": (0, -1),
    "South": (0, 1),
    "East": (1, 0),
    "West": (-1, 0)
}

oppositeDir = lambda x: "North" if x == "South" else "South" if x == "North" else "East" if x == "West" else "West" if x == "East" else None

def findNext(pos: list[tuple[int, int]], matrix: list[list[str]]) -> tuple[int, int]:
    lastPos = pos[0]
    currentPos = pos[1]
    pipe = matrix[currentPos[0]][currentPos[1]]
    dir = pipes[pipe]
    if currentPos[0] + directions[dir[0]][1] == lastPos[0] and currentPos[1] + directions[dir[0]][0] == lastPos[1]:
        nextPos = (currentPos[0] + directions[dir[1]][1], currentPos[1] + directions[dir[1]][0])
    else:
        nextPos = (currentPos[0] + directions[dir[0]][1], currentPos[1] + directions[dir[0]][0])
    return (currentPos, nextPos)



def findStart(pos: tuple[int, int], matrix: list[list[str]]) -> list[tuple[int, int]]:
    returnList = []
    for direction in directions:
        if matrix[pos[0] + directions[direction][1]][pos[1] + directions[direction][0]] in pipes:
            if oppositeDir(direction) in pipes[matrix[pos[0] + directions[direction][1]][pos[1] + directions[direction][0]]]:
                returnList.append((pos[0] + directions[direction][1], pos[1] + directions[direction][0]))
    return returnList

with open("Day 10\\input.txt", "r") as file:
    text = file.read()
    fulltext = text.replace("\n", "")
    start = (fulltext.index("S")//140,fulltext.index("S")%140)
    textMatrix = text.split("\n")
    Pos1 = [start]
    Pos2 = [start]
    startPos = findStart(start, textMatrix)
    Pos1.append(startPos[0])
    Pos2.append(startPos[1])
    count = 1
    Path1 = []
    Path2 = []
    while Pos1[1] != Pos2[1]:
        Pos1 = findNext(Pos1, textMatrix)
        Pos2 = findNext(Pos2, textMatrix)
        count += 1
        Path1.append(Pos1[0])
        Path2.append(Pos2[0])
    print(count)