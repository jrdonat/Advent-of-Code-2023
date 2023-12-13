import re

with open('Day 12\\input.txt') as file:
    input = file.read().split('\n')
    # Example line: .??..??...?##. 1,1,3
    # Possible combinations: .#...#....###.
    # Possible combinations: .#....#...###.
    # Possible combinations: ..#...#...###.
    # Possible combinations: ..#..#....###.
    runningSum = 0
    for line in input:
        splited = line.split(' ')
        numbers = splited[1].split(',')
        blocks = re.sub(' +',' ',splited[0].replace('.',' ')).split(' ')
        blocks = [x for x in blocks if x]
        newstr = splited[0]
        # for number in numbers:
        #     snail = '-' * int(number)
        #     startingIndex = re.search('[?#]', newstr).start()
        #     while newstr[startingIndex-1] == '-':
        #         startingIndex = re.search('[?#]', newstr[startingIndex+1]).start()
        #     newstr = newstr[:startingIndex] + snail + newstr[startingIndex + len(snail):]
