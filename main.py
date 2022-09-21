import random


board = [[1, 2, 3],
         [4, "x", 6],
         [7, 8, 9]]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
    """)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    successfull_tries = 0
    while successfull_tries == 0:

        try:
            move = int(input("Enter your move: "))
        except ValueError:
            print("Invalid move. Try again")
            continue

        if move < 10 and move > 0:
            for i in range(3):
                for j in range(3):
                    if int(move) == board[i][j]:
                        board[i][j] = "o"
                        successfull_tries += 1
        else:
            print("Invalid move. Try again")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    free_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] in nums:
                free_list.append((i, j))
    return free_list

def horizontal_win(sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True

def vertical_win(sign):
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True

def diagonal_win(sign):
    if board[0][0] == board[1][1] == board[2][2] == sign or \
            board[2][0] == board[1][1] == board[0][2] == sign:
        return True

def victory_for(board, sign):
    if horizontal_win(sign) or vertical_win(sign) or diagonal_win(sign) == True:
        display_board(board)
        print(f"Game Over, {sign} wins!")
        return True
    else:
        return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    successfull_tries = 0
    while successfull_tries == 0:
        move = random.randint(1, 10)
        for i in range(3):
            for j in range(3):
                if move == board[i][j]:
                    board[i][j] = "x"
                    successfull_tries += 1

def game_loop():
    while make_list_of_free_fields(board) != []:
        display_board(board)

        enter_move(board)
        if victory_for(board, "o") == True:
            break
        if make_list_of_free_fields(board) == []:
            break
        draw_move(board)
        if victory_for(board, "x") == True:
            break
        if make_list_of_free_fields(board) == []:
            break
    if victory_for(board, "o") == False and victory_for(board, "x") == False:
        display_board(board)
        print("Game is a tie")

game_loop()
