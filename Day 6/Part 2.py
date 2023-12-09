import re
import math
with open("Day 6\\input.txt", "r") as file:
    input = file.read()
    input = input.split("\n")
    times = int(''.join(re.findall(r"\d+",input[0])))
    distances = int(''.join(re.findall(r"\d+",input[1])))
    dis = times * times - 4 * -1 * - distances
    sqrt_val = math.sqrt(abs(dis)) 
    root1 = math.ceil((-times + sqrt_val) / (2 * -1))
    root2 = math.floor((-times - sqrt_val) / (2 * -1))
    diff = root2 - root1 + 1
    print(diff)
