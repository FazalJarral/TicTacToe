import random

board = {
    "1": '_', "2": '_', "3": '_',
    "4": '_', "5": '_', "6": '_',
    "7": '_', "8": '_', "9": '_',

}


def print_board():
    print('   |   |')
    print(' ' + board["1"] + ' | ' + board["2"] + ' | ' + board["3"])
    print('   |   |')
    print(' ' + board["4"] + ' | ' + board["5"] + ' | ' + board["6"])
    print('   |   |')
    print(' ' + board["7"] + ' | ' + board["8"] + ' | ' + board["9"])


def first_turn():
    if random.randint(0, 2) == 0:
        # X is for human
        return "Human"
    else:
        return "Computer"


def get_available_slots():
    return [pos for pos, value in board.items() if value == "_"]


def board_has_space():
    if [item for pos,item in board.items() if item == "_"]:
        return True
    else:
        return False


moves_made = []


def is_winning_move(marker):
    return ((board["7"] == marker and board["8"] == marker and board["9"] == marker) or  # across the bottom
            (board["4"] == marker and board["5"] == marker and board["6"] == marker) or
            (board["1"] == marker and board["2"] == marker and board["3"] == marker) or
            (board["1"] == marker and board["4"] == marker and board["7"] == marker) or
            (board["2"] == marker and board["5"] == marker and board["8"] == marker) or
            (board["3"] == marker and board["6"] == marker and board["9"] == marker) or
            (board["1"] == marker and board["5"] == marker and board["9"] == marker) or
            (board["3"] == marker and board["5"] == marker and board["7"] == marker))


def main():
    found_winner = False

    current_player = first_turn()
    continue_game = True

    while continue_game:

        if current_player == 'Human':
            print("You Will Make the Move")
            board_piece = input("Where Would You Place Your Marker: ")
            if board_has_space():
                if board_piece.isnumeric() and board_piece != 0:

                    if board_piece in moves_made:
                        print("The Block Is Not Empty, Select Another One")
                    else:
                        board[board_piece] = "X"
                        moves_made.append(board_piece)
                        print_board()

                        if is_winning_move("X"):
                            found_winner = True
                            continue_game = False

                        else:
                            current_player = 'Computer'

                else:
                    print("Please Select From 1-10")
        else:
            # Computer will make a move
            print("Computer Will Make the Move")
            if board_has_space():
                empty_space = get_available_slots()

                move = random.choice(empty_space)
                board[move] = "O"
                moves_made.append(move)
                print_board()
                if is_winning_move("O"):
                    found_winner = True
                    continue_game = False
                else:
                    current_player = 'Human'



    else:
        if found_winner:
            print(f'{current_player} has WON!!!')
        else:
            print("Its a draw")


if __name__ == "__main__":
    main()
