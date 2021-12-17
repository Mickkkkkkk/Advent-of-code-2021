"""
inverted index: num er term; board,row,col er posting
en row/col counter for hver board
boards = flate lister med numre i brett
"""

def get_loser(inverted, board_counters, draws, boards):
    most_turns = 0
    loser = 0
    for i, count in enumerate(board_counters):
        print(i)
        not_won = True
        turn = 0
        while not_won and turn < len(draws):
            for tup in inverted.get(draws[turn], []):
                if tup[0] == i:
                    count[0][tup[1]] += 1
                    count[1][tup[2]] += 1
                    if count[0][tup[1]] == 5 or count[1][tup[2]] == 5:
                        not_won = False
                        if turn >= most_turns:
                            print("NEW")
                            loser = i
                            most_turns = turn
            turn += 1
    return sum([x for x in boards[loser] if x not in draws[:most_turns+1]]) * draws[:most_turns+1][-1]

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

print(get_loser(inverted_boards, board_counters, draws, boards))
