import re
numbersList = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

def generateNumbersByLine(line: str) -> list[str]:
    numbers = []
    currentIndex = 0
    for _ in range(len(line)):
        match = re.search(r"\d|"+regex, line)
        if not match:
            break
        currentIndex = match.start()
        numbers.append(match.group())
        line = line[currentIndex+1:]
    print(numbers)
    return numbers
    

with open("Day 1\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    runningSum = 0
    for line in input:
        regex = "|".join(numbersList.keys())
        # numbers = re.findall(r"\d|"+regex, line)
        numbers = generateNumbersByLine(line)
        if len(numbers[0]) > 1:
            runningSum += numbersList[numbers[0]]*10
        else:
            runningSum += int(numbers[0])*10
        if len(numbers[-1]) > 1:
            runningSum += numbersList[numbers[-1]]
        else:
            runningSum += int(numbers[-1])
    print(runningSum)
