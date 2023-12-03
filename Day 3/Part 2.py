import re
symbols = ['*']

# Observation: No number is ever touching two symbols

stars = {
    # Example: (index, lineindex) : [numbers...]
}

with open("Day 3\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    runningSum = 0
    for line in input:
        try:
            lastLine = input[input.index(line)-1]
        except:
            lastLine = ""
        try:
            nextLine = input[input.index(line)+1]
        except:
            nextLine = ""
        numbers = re.findall(r"\d+", line)
        currentIndex = 0
        finds = []
        for number in numbers:
            num = re.search(rf"{number}", line[currentIndex:])
            span = num.span()
            span = (span[0]+currentIndex, span[1]+currentIndex)
            currentIndex = span[1]
            if span[0] > 0:
                if line[span[0]-1] in symbols:
                    try:
                        stars[(span[0]-1, input.index(line))].append(number)
                    except:
                        stars[(span[0]-1, input.index(line))] = [number]
                    continue
            if span[1] < len(line):
                if line[span[1]] in symbols:
                    try:
                        stars[(span[1], input.index(line))].append(number)
                    except:
                        stars[(span[1], input.index(line))] = [number]
                    continue
            if lastLine != "":
                for i in range(max(span[0]-1,0), min(span[1]+1, len(lastLine))):
                    if lastLine[i] in symbols:
                        try:
                            stars[(i, input.index(lastLine))].append(number)
                        except:
                            stars[(i, input.index(lastLine))] = [number]
                        break
            if nextLine != "":
                for i in range(max(span[0]-1,0), min(span[1]+1, len(nextLine))):
                    if nextLine[i] in symbols:
                        try:
                            stars[(i, input.index(nextLine))].append(number)
                        except:
                            stars[(i, input.index(nextLine))] = [number]
                        break
    for star in stars:
        if len(stars[star]) == 2:
            runningSum += int(stars[star][0])*int(stars[star][1])
    print(runningSum)


