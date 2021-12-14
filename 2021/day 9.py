# Advent of Code - 2021
# Day 9

# file stuff
file = open("day 9.txt", "r")
input = [x.strip() for x in file.readlines()]
file.close()

# transform input
matrix = []
for line in input:
    row = [int(char) for char in line]
    matrix.append(row)

def is_lowest_of_neighbors(matrix, i,j):
    col_len = len(matrix)
    row_len = len(matrix[0])

    # check out of bounds
    directions = []
    # left
    if not i - 1 < 0:
        directions.append(matrix[i-1][j])
    # up
    if not j - 1 < 0:
        directions.append(matrix[i][j-1])
    # right
    if not i + 1 > col_len -1:
        directions.append(matrix[i+1][j])
    # down
    if not j + 1 > row_len -1:
        directions.append(matrix[i][j+1])
    cur_val = matrix[i][j]

    if all([d > cur_val for d in directions]):
        return True

    return False

# find low points
def find_low_points(matrix):
    low_points = []

    for i, row in enumerate(matrix):
        for j, point in enumerate(row):
            if is_lowest_of_neighbors(matrix, i,j):
                low_points.append((i,j))

    return low_points

def calc_risk_level(points):
    return sum([int(x)+1 for x in points])

def find_basin_size(point, matrix):
    col_len = len(matrix)
    row_len = len(matrix[0])

    nodes = [point]
    visited = set()
    visited.add(point)
    no_new = False
    while len(nodes) > 0:
        i,j = nodes.pop()
        # left
        if not i - 1 < 0 and matrix[i-1][j] < 9 and (i-1,j) not in visited:
            visited.add((i-1,j))
            nodes.append((i-1,j))
        # up
        if not j - 1 < 0 and matrix[i][j-1] < 9 and (i,j-1) not in visited:
            visited.add((i, j-1))
            nodes.append((i, j-1))
        # right
        if not i + 1 > col_len -1 and matrix[i+1][j] < 9 and (i+1,j) not in visited:
            visited.add((i+1,j))
            nodes.append((i+1,j))
        # down
        if not j + 1 > row_len -1 and matrix[i][j+1] < 9 and (i,j+1) not in visited:
            visited.add((i,j+1))
            nodes.append((i,j+1))

    print(visited)
    return len(visited)

def get_largest_basins(points, matrix):
    basins = []
    for point in points:
        basins.append(find_basin_size(point, matrix))
    
    largest = sorted(basins, reverse=True)
    return largest[0] * largest[1] * largest[2]

# part two answer
print(get_largest_basins(find_low_points(matrix), matrix))

# part 1 answer
# print(calc_risk_level(find_low_points(matrix)))



# calcualte risk score