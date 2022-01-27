# PREAMBLE
def check_win(board):
    # Horizontal
    for row in board:
        if row.count(-1) == 5:
            return True

    # Vertical
    for column in range(5):
        n_marked = 0
        for row in board:
            if row[column] == -1:
                n_marked += 1
        if n_marked == 5:
            return True

    return False


def mark_number(board, number):
    for row in range(5):
        for col in range(5):
            if board[row][col] == number:
                board[row][col] = -1


with open("input") as f:
    marks = [int(n) for n in f.readline().split(',')]
    boards = [line.split(' ') for line in f.read().split('\n') if line != '']
    boards = [[int(x) for x in n if x.isnumeric()] for n in boards]
    boards = [boards[i:i + 5] for i in range(0, len(boards), 5)]


# PART 1
def calculate_first_winning_board(_marks, _boards):
    for mark in _marks:
        for board in _boards:
            mark_number(board, mark)
            if check_win(board):
                answer = 0
                for row in range(5):
                    for col in range(5):
                        if board[row][col] != -1:
                            answer += board[row][col]

                return answer * mark


print(calculate_first_winning_board(marks, boards))  # 25410 is correct


# PART 2
def calculate_last_winning_board(_marks, _boards):
    for mark in _marks:
        for board in _boards:
            mark_number(board, mark)

        _boards = [b for b in _boards if not check_win(b)]

        if len(_boards) == 1:
            return calculate_first_winning_board(_marks, _boards)


print(calculate_last_winning_board(marks, boards))  # 2730 is Correct!
