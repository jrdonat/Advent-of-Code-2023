import re

with open("Day 4\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    runningSum = 0
    for line in input:
        matches = 0
        gameId = re.search(r"\d+", line) # Usually in these problems u need the game ID. I don't need it here, but I'm too lazy to remove it
        line = line[gameId.span()[1]+2:]
        line = line.split(" | ")
        winningNumbers = line[0].split(" ")
        winningNumbers = [int(i) for i in winningNumbers if i != ""]
        myNumbers = line[1].split(" ")
        myNumbers = [int(i) for i in myNumbers if i != ""]
        for number in myNumbers:
            if number in winningNumbers:
                matches += 1
        runningSum += 2**(matches-1) if matches > 0 else 0
    print(runningSum)