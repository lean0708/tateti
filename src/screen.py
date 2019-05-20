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


def print_to_screen(str_message, clear_all=True):
    if clear_all:
        print_header()
    print(str_message)


def ask_something(question, valid_answers, clear_all=True):
    # python 2.7 fix for input command
    try:
        input = raw_input
    except NameError:
        pass
    if clear_all:
        print_header()
    answer = ""
    answer_invalid = True
    while answer_invalid:
        answer = input(question)
        if answer not in valid_answers:
            print_to_screen("Please select one of this options: {}".format(valid_answers), clear_all=False)
        else:
            answer_invalid = False
    return answer



