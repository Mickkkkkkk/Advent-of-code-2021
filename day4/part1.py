"""
inverted index: num er term; board,row,col er posting
en row/col counter for hver board
"""

def get_winner(inverted, board_counters, draws, boards):
    for i, num in enumerate(draws):
        for posting in inverted.get(num, []):
            board_counters[posting[0]][0][posting[1]] += 1 # i her ikke riktig, ingenting er riktig her
            board_counters[posting[0]][1][posting[2]] += 1
            if board_counters[posting[0]][0][posting[1]] == 5 or board_counters[posting[0]][1][posting[2]] == 5:
                unmarked_sum = sum([x for x in boards[posting[0]] if x not in draws[:i+1]])
                return unmarked_sum * num

file = open("input.txt")
draws = [int(x) for x in file.readline().split(",")]

inverted_boards = {}
boards = []
board_counters = []

i = -1
row = 0
for line in file:
    if line == "\n":
        row = 0
        i += 1
        board_counters.append(([0 for x in range(5)], [0 for x in range(5)]))
        boards.append([])
    else:
        for col, num in enumerate(line.split()):
            if inverted_boards.get(int(num), None) == None:
                inverted_boards[int(num)] = []
            inverted_boards[int(num)].append((i, row, col))
            boards[i].append(int(num))
        row += 1

print(get_winner(inverted_boards, board_counters, draws, boards))
