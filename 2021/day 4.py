# Advent of Code - 2021
# Day 4

file = open("day 4.txt", "r")
input = file.readlines()
file.close()

cleaned_input = [x.strip() for x in input]

bingo_numbers = cleaned_input.pop(0).split(',')
bingo_numbers = [int(x) for x in bingo_numbers]

# build the bingo boards
class Node:
    def __init__(self, number):
        self.number = int(number)
        self.on = False
    
    def mark(self):
        self.on = True

    def __str__(self):
        return f"number: {self.number}, on: {self.on}"

class Board:
    def __init__(self, matrix):
        self.board = matrix
        self.rotatedBoard = list(zip(*matrix[::-1])) # dope but unobvious hack to transpose 2d matrix

    def mark(self, number):
        for line in self.board:
            for node in line:
                if node.number == number:
                    node.mark()
        
        for line in self.rotatedBoard:
            for node in line:
                if node.number == number:
                    node.mark()
        
    def hasBingo(self):
        for line in self.board:
            if all(node.on for node in line):
                return True

        for line in self.rotatedBoard:
            if all(node.on for node in line):
                return True
        return False

    def getScore(self):
        sum = 0
        for line in self.board:
            for node in line:
               if not node.on:
                   sum += node.number

        return sum

    def __str__(self):
        for line in self.board:
            for node in line:
                print(node)
            print('\n')
        
        for line in self.rotatedBoard:
            for node in line:
                print(node)
            print('\n')
        return ''

# testing to make sure nodes mark themselves properly
# test = Node(42)
# test.mark()

boards = []
board = []

# build the boards
for line in cleaned_input:
    if line == "":
        continue

    nums = line.split()
    board.append([Node(x) for x in nums])

    # OOF - originally i had this checking before the 2 lines above, which meant
    # on the last board we never added the board. This made it appear as if the rest of
    # the code was incorrect, and was terrible to debug. This is a clear example of wrapping this
    # separate functionality into a function with a test to ensure it works before moving on
    if len(board) == 5:
        boards.append(Board(board))
        board = []

quit = False
bingoed_boards = set()
boards_set = set(boards)

for num in bingo_numbers:
    for board in list(boards_set - bingoed_boards):

        board.mark(num)
        if board.hasBingo():
            bingoed_boards.add(board)

            if len(bingoed_boards) == len(boards):
                quit = True

                print(board.getScore() * num)
    if quit:
        break


