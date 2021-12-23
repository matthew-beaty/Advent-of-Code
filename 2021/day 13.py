# Advent of Code - 2021
# Day 13

file = open("day 13.txt", "r")
input = [x.strip() for x in file.readlines()]
file.close()

coords = input[:input.index('')]
folds = input[input.index('')+1:]
points = [[int(y) for y in x.split(',')] for x in coords]

def fold_value(value, fold_line):
    if value > fold_line:
        dist = value - fold_line
        value = fold_line - dist
    return value

def fold_points(points, fold_line, fold_along_y):
    # create unique points so we can remove dupes
    points_set = set()

    for x,y in points:
        if fold_along_y:
            y = fold_value(y, fold_line)
        else:
            x = fold_value(x, fold_line)
        
        points_set.add((x,y))

    return points_set

def folded(points, fold_instruction):
    line, num = fold_instruction.split('=')
    fold_along_y = False
    if 'y' in line:
        fold_along_y = True
    
    return fold_points(points, int(num), fold_along_y)

new_points = points
for f in folds:
    new_points = folded(new_points, f)

chart = [['.' for i in range(40)] for j in range(40)]

for x,y in new_points:
    chart[x][y] = '#'

for row in chart:
    print(''.join(row))
