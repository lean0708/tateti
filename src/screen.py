from os import system, name

NEW_LINE_CHARACTER = "\n"
GAME_HEADER = """
****************************
**    Tic-Tac-Toe Game    **
****************************
"""


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def print_header():
    clear_screen()
    print GAME_HEADER


def print_to_screen(str):
    print_header()
    print(str)


def ask_something(question, valid_answers):
    # python 2.7 fix for input command
    try:
        input = raw_input
    except NameError:
        pass
    print_header()
    answer_invalid = True
    while answer_invalid:
        answer = input(question)
        if answer not in valid_answers:
            print_to_screen("Please select one of this options: {}".format(valid_answers))
        else:
            answer_invalid = False
    return answer


def print_board(board, letters):
    string_board = ""
    for row in board:
        for cell_value in row:
            string_board += "[{}]".format(letters[cell_value])
        string_board += NEW_LINE_CHARACTER
    print(NEW_LINE_CHARACTER)
    print(string_board)


