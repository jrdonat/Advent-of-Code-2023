import re
maxes = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}
with open("Day 2\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    sumSuccessIds = 0
    for line in input:
        gameId = re.search(r"\d+", line)
        line = line[gameId.span()[1]+2:]
        pulls = line.split("; ")
        success = True
        for pull in pulls:
            pull = pull.split(", ")
            for color in pull:
                color = color.split(" ")
                if int(color[0]) > maxes[color[1]]:
                    success = False
                    break
            if not success:
                break
        if success:
            sumSuccessIds += int(gameId.group())
    print(sumSuccessIds)
