# Advent of Code - 2021
# Day 11

file = open("day 11.txt", "r")
input = [x.strip() for x in file.readlines()]
file.close()

# print(input)
cleaned_input = []
for item in input:
    new_list = []
    for char in item:
        new_list.append(int(char))
    cleaned_input.append(new_list)

# print(cleaned_input)

steps = 1
m = 0
temp_matrix = cleaned_input
# print(temp_matrix)
flashes = 0
print('started')
while m < 1000:
    print(m)
    has_flashed = set()
    go_to_next = False
    # add 1 to everything
    for i, row in enumerate(temp_matrix):
        for j,num in enumerate(row):
            temp_matrix[i][j] += 1

    # for each > 9, flash(), add item to hasFlashed

    def left(i,j):
        if j-1 < 0:
            return None
        temp_matrix[i][j-1] += 1
    def right(i,j):
        if j+1 > 9:
            return None
        temp_matrix[i][j+1] += 1
    def down(i,j):
        if i-1 < 0:
            return None
        temp_matrix[i-1][j] += 1
    def up(i,j):
        if i+1 > 9:
            return None
        temp_matrix[i+1][j] += 1
    def upleft(i,j):
        if i+1 > 9 or j - 1 < 0:
            return None
        temp_matrix[i+1][j-1] += 1
    def upright(i,j):
        if i+1 > 9 or j + 1 > 9:
            return None
        temp_matrix[i+1][j+1] += 1
    def downright(i,j):
        if i -1 < 0 or j + 1 > 9:
            return None
        temp_matrix[i-1][j+1] += 1
    def downleft(i,j):
        if i -1 < 0 or j - 1 < 0:
            return None
        temp_matrix[i-1][j-1] += 1
    
    directions = [
        left, right, up, down, upleft, upright, downleft, downright
    ]

    # do flashes 
    while not go_to_next:
        flashed = False
        for i, row in enumerate(temp_matrix):
            for j, num in enumerate(row):
                if temp_matrix[i][j] > 9 and (i,j) not in has_flashed:
                    flashes += 1
                    for direction in directions:
                        result = direction(i,j)
                    has_flashed.add((i,j))
                    flashed = True
        
        if not flashed:
            go_to_next = True


    # reset flashes to 0


    for i, row in enumerate(temp_matrix):
        for j, num in enumerate(row):
            if temp_matrix[i][j] > 9:
                temp_matrix[i][j] = 0
    has_flashed = set()
    if all([item == 0 for row in temp_matrix for item in row]):
        print('weeee')
        print(m+1)
    m += 1
        
print(flashes)
# Idea 1: 
# Step 1
#   add 1 everywhere
#   for each > 9, flash(), add item to hasFlashed
# loop until no 9's not in hasFlashed
# next step

