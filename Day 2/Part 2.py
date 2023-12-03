import re
with open("Day 2\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    runningSum = 0
    for line in input:
        gameId = re.search(r"\d+", line)
        line = line[gameId.span()[1]+2:]
        pulls = line.split("; ")
        maxBlue = 0
        maxGreen = 0
        maxRed = 0
        for pull in pulls:
            pull = pull.split(", ")

            for color in pull:
                color = color.split(" ")
                if color[1] == "red":
                    maxRed = max(maxRed, int(color[0]))
                elif color[1] == "green":
                    maxGreen = max(maxGreen, int(color[0]))
                elif color[1] == "blue":
                    maxBlue = max(maxBlue, int(color[0]))
        print(maxRed, maxGreen, maxBlue)
        runningSum += maxRed*maxGreen*maxBlue

    print(runningSum)
