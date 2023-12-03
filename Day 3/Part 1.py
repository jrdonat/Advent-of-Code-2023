import re
symbols = ['-','@','#','*','=','+','%','/','$','&']

# Observation: No number is ever touching two symbols

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
        for number in numbers:
            num = re.search(rf"{number}", line[currentIndex:])
            span = num.span()
            span = (span[0]+currentIndex, span[1]+currentIndex)
            currentIndex = span[1]
            if span[0] > 0:
                if line[span[0]-1] in symbols:
                    runningSum += int(number)
                    continue
            if span[1] < len(line):
                if line[span[1]] in symbols:
                    runningSum += int(number)
                    continue
            if lastLine != "":
                for i in range(max(span[0]-1,0), min(span[1]+1, len(lastLine))):
                    if lastLine[i] in symbols:
                        runningSum += int(number)
                        break
            if nextLine != "":
                for i in range(max(span[0]-1,0), min(span[1]+1, len(nextLine))):
                    if nextLine[i] in symbols:
                        runningSum += int(number)
                        break
    print(runningSum)


