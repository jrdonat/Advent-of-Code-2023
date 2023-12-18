directions = {
    "North": (0, -1),
    "South": (0, 1),
    "East": (1, 0),
    "West": (-1, 0)
}
panels = {
    '/': lambda x: 'North' if x == 'East' else 'East' if x == 'North' else 'South' if x == 'West' else 'West' if x == 'South' else None,
    '\\': lambda x: 'North' if x == 'West' else 'West' if x == 'North' else 'South' if x == 'East' else 'East' if x == 'South' else None,
    '|': lambda x: 'North' if x == 'North' else 'South' if x == 'South' else ('North', 'South') if x == 'East' or x== 'West' else None,
    '-': lambda x: 'East' if x == 'East' else 'West' if x == 'West' else ('East', 'West') if x == 'North' or x == 'South' else None,
}
cache = {}
workers = [
    ['East', (-1,0)]
]

def getNextDirection(direction: str, panel: str) -> str:
    return panels[panel](direction)

with open("Day 16\\input.txt","r") as file:
    input = file.read().split('\n')
    while len(workers) > 0:
        for worker in workers:
            worker[1] = (worker[1][0] + directions[worker[0]][0], worker[1][1] + directions[worker[0]][1])
            if worker[1][0] < 0 or worker[1][0] >= len(input[0]) or worker[1][1] < 0 or worker[1][1] >= len(input):
                workers.remove(worker)
                continue
            if input[worker[1][1]][worker[1][0]] in panels:
                dirs = getNextDirection(worker[0], input[worker[1][1]][worker[1][0]])
                if len(dirs) == 2:
                    workers.append([dirs[1], worker[1]])
                    worker[0] = dirs[0]
                else:
                    worker[0] = dirs
            if tuple(worker) in cache:
                workers.remove(worker)
                continue
            cache[tuple(worker)] = True
    temp = {}
    for i in cache:
        val = i[1]
        temp[val] = True
    print(len(temp))
