with open('Day 14\\input.txt') as file:
    input = file.read().split('\n')
    input = [list(x) for x in input]
    for i, line in enumerate(input):
        for j, rock in enumerate(line):
            counter = 1
            if rock != 'O': continue
            while i != 0 and input[i-counter][j] == '.' and i-counter >= 0:
                input[i-counter][j] = 'O'
                input[i-counter+1][j] = '.'
                counter += 1
    load = 0
    for i, line in enumerate(input):
        for rock in line:
            if rock == 'O':
                load += len(input) - i
    print(load)