import sys

basins = {}
land = {}
dimension = int(sys.stdin.readline().strip())

for row, line in enumerate(sys.stdin):
    line = line.strip()
    value = line.split()
    value = [int(num) for num in value]
    for col in range(dimension):
        land[(row, col)] = {}
        land[(row, col)]['elevation'] = value[col]

def lowest_neighbor(row, col):
    if 'lowest_neighbor' in land[(row, col)]:
        return land[(row, col)]['lowest_neighbor']

    lowest = min(neighbors(row, col) + [(row, col)], key=lambda x: land[x]['elevation'])

    land[(row, col)]['lowest_neighbor'] = lowest
    if lowest == (row, col):
        land[(row, col)]['sink'] = lowest
        basins[lowest] = 0

    return lowest

def sink(row, col):
    if 'sink' not in land[(row, col)]:
        lowest = lowest_neighbor(row, col)
        land[(row, col)]['sink'] = sink(lowest[0], lowest[1])
    return land[(row, col)]['sink']

def neighbors(row, col):
    adjacent = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    return [neighbor for neighbor in adjacent if neighbor in land]

for row in range(dimension):
    for col in range(dimension):
        basins[sink(row, col)] += 1

basin_sizes = basins.values()
basin_sizes.sort()
basin_sizes.reverse()
output = ' '.join([str(num) for num in basin_sizes])
sys.stdout.write(output)
