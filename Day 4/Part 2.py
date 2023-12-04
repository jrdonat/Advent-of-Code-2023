import re
#* Example line: Card   1:  8 86 59 90 68 52 55 24 37 69 | 10 55  8 86  6 62 69 68 59 37 91 90 24 22 78 61 58 89 52 96 95 94 13 36 81

scratchCards = [1]

with open("Day 4\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    scratchCards *= len(input)
    for i, line in enumerate(input):
        winningNumbers = line[9:line.index(" | ")].split(" ")
        winningNumbers = [int(i) for i in winningNumbers if i != ""]
        myNumbers = line[line.index(" | ")+3:].split(" ")
        myNumbers = [int(i) for i in myNumbers if i != ""]
        matches = {}
        for _ in range(scratchCards[i]):
            for number in myNumbers:
                if number in winningNumbers:
                    try:
                        matches[number] += 1
                    except:
                        matches[number] = 1
        