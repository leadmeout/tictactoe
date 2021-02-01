import random

"""

OPEN ISSUES:

#1. If user wins the game, the computer should not be able to play.

Example: The game should end after the user played 9. Likely have to split user turn and comp turn into two functions

    Where would you like to play? Pick a number between 1 - 9:
    9
    The computer plays 1.
    Congratulations, you won!

            ___________________
            |     |     |     |
            |  x  |  x  |  x  |
            |     |     |     |
            |-----------------|
            |     |     |     |
            |  4  |  5  |  6  |
            |     |     |     |
            |-----------------|
            |     |     |     |
            |  o  |  o  |  o  |
            |     |     |     |
            |-----------------|

##############################################################################

#2. A win on a full board should count as a win and not a tie.

Example: If the user plays 4, it should be a win. Program currently prioritizes full board over winning condition.

            ___________________
            |     |     |     |
            |  x  |  o  |  o  |
            |     |     |     |
            |-----------------|
            |     |     |     |
            |  4  |  o  |  x  |
            |     |     |     |
            |-----------------|
            |     |     |     |
            |  x  |  x  |  o  |
            |     |     |     |
            |-----------------|

    Where would you like to play? Pick a number between 1 - 9:
    4
    Board is full!
    Wins: 0  Losses: 0
    Do want to play Again?(y/n)

##############################################################################

"""


def ex_or_oh():
    """
    Define which character to play with, either x or o.
    User can pick from list of two choices. The computer will take the remaining choice.
    """

    choices = ['x', 'o']

    # while loop until user picks valid character, either x or o
    while True:

        user_character = input("Would you like to play as X or O?\n").lower()

        if user_character not in choices:
                print("Please choose either X or O!")
        else:
            # remove user choice from list
            choices.remove(user_character)
            # assign remaining choice to the computers
            comp_character = choices[0]
            #return choices
            return user_character, comp_character


def pick_square(user_square_picks, comp_square_picks, available_squares):

    """
    This function asks the player in which square they would like to place their character.
    The computer will pick a random number after to play their character.
    If all squares have been filled, meaning available_squares is empty, return False
    """

    if len(available_squares) > 0:
        square_choice = int(input("Where would you like to play? Pick a number between 1 - 9: \n"))

        while square_choice not in available_squares:
            print("That square has already been played!")
            square_choice = int(input("Where would you like to play? Pick a number between 1 - 9: \n"))
        else:
            user_square_picks.append(square_choice)
            available_squares.remove(square_choice)
    else:
        print("Board is full!")
        return False

    if len(available_squares) > 0:
        comp_square_choice = int(random.choice(available_squares))
        comp_square_picks.append(comp_square_choice)
        available_squares.remove(comp_square_choice)
        print(f"The computer plays {comp_square_choice}.")
        return square_choice, comp_square_choice
    else:
        print("Board is full!")
        return False


def display_board(user_square_picks, user_character, comp_square_picks, comp_character):

    """
    Function to refresh and display the current game board.
    Takes in the lists user_square_picks and comp_square_picks to replace the numbers with user_character and comp_character (characters are either X or O)
    """

    board="""
        ___________________
        |     |     |     |
        |  7  |  8  |  9  |
        |     |     |     |
        |-----------------|
        |     |     |     |
        |  4  |  5  |  6  |
        |     |     |     |
        |-----------------|
        |     |     |     |
        |  1  |  2  |  3  |
        |     |     |     |
        |-----------------|
        """

    # for i in range 1 - 10 since there are 9 fields on the board
    for i in range(1, 10):
        # if the number i is in the list of numbers the user has picked
        # replace the str(i) in the blankboard with the users character (x or o)
        if (i in user_square_picks):
            board = board.replace(str(i), user_character)
        # repeat above steps for computer
        elif (i in comp_square_picks):
            board = board.replace(str(i), comp_character)
    # output the board to the screen
    print(board)


def check_victory_condition(user_square_picks, comp_square_picks, played_squares, win_loss_record):
    """
    Function to check if user or computer picked the numbers required for a win, eg. 1, 2, 3 = three in a row.
    One set of winning numbers is defined as a list. All sets are lists within a larger list containing said sets.
    """

    # winning numbers
    victory_conditions = [[1, 4, 7], [1, 5, 9], [1, 2, 3],
                        [4, 5, 6], [7, 8, 9], [3, 5, 7],
                        [3, 6, 9], [2, 5, 8]]

    # iterate through each list (remember each list contains one winning condition) within victory conditions
    for winning_numbers in victory_conditions:
        count = 0
        # compare the list to the numbers selected by the user
        # user_square_picks is a list of numbers the user has selected to play/mark with their character
        for num in user_square_picks:
            # if the number selected by the user is in the winning number list, increase count by 1
            # a total of three is needed to win (eg. user plays 1, 5, 4, 7, they match with 1, 4, 7 required for a vertical win in the left column)
            if num in winning_numbers:
                count += 1
        # if three numbers in user_square_picks matches with a list in victory conditions, the count will be three
        if count == 3:
            # increase user win record by one
            win_loss_record['user'] += 1
            print("Congratulations, you won!")
            # return false to trigger win condition for while loop in run_game()
            return False

    # same as above excpet for computer victory
    for winning_numbers in victory_conditions:
        count = 0
        for num in comp_square_picks:
            if num in winning_numbers:
                count += 1
        if count == 3:
            win_loss_record['comp'] += 1
            print("You lost! The computer won!")
            return False


def replay(win_loss_record):
    """
    A function used to restart the run_game() function if the user would like to play again.
    This function is only called once within run_game() and calls run_game() again if restart == "y".
    """
    # print out current win loss record
    print(f"Wins: {win_loss_record['user']}  Losses: {win_loss_record['comp']}")

    #request restart
    restart = input("Do want to play Again?(y/n)\n")

    # if user would like to restart, start the run_game() function again
    if restart == "y" or restart == "Y":
        print("Starting game again")
        run_game()
    # else print out "thank you for playing"
    else:
        print("Thank you for playing!")


def load_game():
    """
    This function returns the required variables for run_game() to work.
    It also executes the function ex_or_oh which requires the user to choose their character, either x or o.
    """

    available_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    user_square_picks = []
    comp_square_picks = []
    played_squares = user_square_picks + comp_square_picks

    # Define characters for user and computer
    user_character, comp_character = ex_or_oh()

    return available_squares, user_square_picks, comp_square_picks, played_squares, user_character, comp_character


# initializes win_loss_record outside of while loop and run_game function so the values are not reset after each round
win_loss_record = {"user" : 0, "comp" : 0}

def run_game():
    """
    Main function to run the TTT game. Initializes required variables for while loop by calling load_game() and assign its output to said variables.
    """

    # initializes variables through load_game() function
    available_squares, user_square_picks, comp_square_picks, played_squares, user_character, comp_character = load_game()

    # flag used for while loop condition
    play_game = True

    # while play_game is true, execute code block
    while play_game:
        # if check_victory_condition does not return false (which would indicate a victory condition has been met)
        if (check_victory_condition(user_square_picks, comp_square_picks, played_squares, win_loss_record) != False):
            # update and display the game board by calling the display_board function
            display_board(user_square_picks, user_character, comp_square_picks, comp_character)
            # pick square will return false if the board is full
            # if the board is full, exit the loop and execute replay()
            if pick_square(user_square_picks, comp_square_picks, available_squares) == False:
                break
        else:
            # if victory condition has been met (victory_condition returns false), display the winning board
            # (basically just running the display_board function again with the last characters played)
            display_board(user_square_picks, user_character, comp_square_picks, comp_character)
            # exit the while loop by setting the while condition to false
            play_game = False

    #ask to play again
    replay(win_loss_record)


if __name__ == '__main__':
    run_game()
