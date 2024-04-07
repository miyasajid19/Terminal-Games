def tictactoe():
    import random
    row1 = ['_', '0', '_', '|', '_', '1', '_', '|', '_', '2', '_']
    row2 = ['_', '3', '_', '|', '_', '4', '_', '|', '_', '5', '_']
    row3 = [' ', '6', ' ', '|', ' ', '7', ' ', '|', ' ', '8', ' ']
    print("".join(row1))
    print("".join(row2))
    print("".join(row3))
    validinput = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    turn = 'O'
    playerO = []
    playerX = []
    
    winning_pattern = [
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
        {0, 4, 8}, {2, 4, 6}
    ]

    for _ in range(9):
        user = int(input(f"Enter among {validinput}: "))
        while user not in validinput:
            user = int(input(f"Invalid input! Enter among {validinput}: "))
        validinput.remove(user)

        update_board(user, turn, row1, row2, row3)
        print_board(row1, row2, row3)

        if turn == 'O':
            playerO.append(user)
        else:
            playerX.append(user)

        winner = check_winner(playerO if turn == 'O' else playerX, winning_pattern)
        if winner:
            print(f"Player {turn} won!")
            return
        
        turn = 'X' if turn == 'O' else 'O'

    print("It's a draw!")

def update_board(user, turn, row1, row2, row3):
    if user == 0:
        row1[1] = turn
    elif user == 1:
        row1[5] = turn
    elif user == 2:
        row1[9] = turn
    elif user == 3:
        row2[1] = turn
    elif user == 4:
        row2[5] = turn
    elif user == 5:
        row2[9] = turn
    elif user == 6:
        row3[1] = turn
    elif user == 7:
        row3[5] = turn
    elif user == 8:
        row3[9] = turn

def print_board(row1, row2, row3):
    print("".join(row1))
    print("".join(row2))
    print("".join(row3))

def check_winner(player_moves, winning_pattern):
    from itertools import combinations
    if len(player_moves) >= 3:
        patterns = list(combinations(player_moves, 3))
        for pattern in patterns:
            pattern_set = set(pattern)
            for win_pattern in winning_pattern:
                if win_pattern.issubset(pattern_set):
                    return True
    return False

tictactoe()
