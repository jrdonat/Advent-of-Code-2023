import re
import math
with open("Day 6\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    times = re.findall(r"\d+",input[0])
    distances = re.findall(r"\d+",input[1])
    times = [int(x) for x in times]
    distances = [int(x) for x in distances]
    runningSum = 1
    for i, v in enumerate(times):
        dis = v * v - 4 * -1 * - distances[i]
        sqrt_val = math.sqrt(abs(dis)) 
        root1 = math.ceil((-v + sqrt_val) / (2 * -1))
        root2 = math.floor((-v - sqrt_val) / (2 * -1))
        diff = root2 - root1 + 1
        runningSum *= diff
    print(runningSum)
