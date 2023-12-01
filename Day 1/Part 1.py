import re
with open("Day 1\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    runningSum = 0
    for line in input:
        numbers = re.findall(r"\d", line)
        if len(numbers) > 1:
            runningSum += int(numbers[0])*10
            runningSum += int(numbers[-1])
        else:
            runningSum += int(numbers[0])*11
    print(runningSum)