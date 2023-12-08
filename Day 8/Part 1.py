with open("Day 8\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    lr = input[0]
    dict = {}
    for line in input[2:]:
        line = line.split(" = ")
        dict[line[0]] = line[1]
    
    def getsplice(count: int) -> str:
        if lr[count%len(lr)] == "L":
            return slice(1,4)
        else:
            return slice(6,9)
    
    count = 0
    index = 'AAA'
    while index != 'ZZZ':
        index = dict[index][getsplice(count)]
        count += 1
    print(count)