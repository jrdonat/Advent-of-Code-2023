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
        matches = 0
        for number in myNumbers:
            if number in winningNumbers:
                matches += 1
        for j in range(matches):
            if i+j+1 < len(scratchCards):
                scratchCards[i+j+1] += 1*scratchCards[i]
    print(sum(scratchCards))
