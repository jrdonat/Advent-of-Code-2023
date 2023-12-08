import math
with open("Day 8\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    lr = input[0]
    directions = {}
    for line in input[2:]:
        line = line.split(" = ")
        directions[line[0]] = line[1]
    def getsplice(count: int) -> str:
        if lr[count%len(lr)] == "L":
            return slice(1,4)
        else:
            return slice(6,9)
    keys = [key for key in directions.keys() if key[-1] == "A"]
    numbers = []
    for key in keys:
        count = 0
        while key[-1] != 'Z':
            key = directions[key][getsplice(count)]
            count += 1
        numbers.append(count)
    print(math.lcm(*numbers))
