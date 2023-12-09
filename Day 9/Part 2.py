with open("Day 9\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    runnningSum = 0
    for line in input:
        pyramid = [line.split(" ")]
        pyramid[0] = [int(x) for x in pyramid[0]]
        while any(x != 0 for x in pyramid[-1]):
            newNums = [pyramid[-1][i+1] - pyramid[-1][i] for i in range(len(pyramid[-1])-1)]
            pyramid.append(newNums)
        pyramid.reverse()
        for i, v in enumerate(pyramid[1:]):
            v.insert(0, v[0] - pyramid[i][0])
        runnningSum += pyramid[-1][0]
    print(runnningSum)
