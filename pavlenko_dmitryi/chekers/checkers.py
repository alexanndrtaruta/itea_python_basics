import random


def coordin(param1, param2):
    """
    This function finds the starting coordinates of the checker and the coordinates of the move.
    :param param1: checkers coordinates
    :param param2: travel coordinates
    :type param1: list
    :type param2:   list
    :return: decrypted coordinates
    :rtype:   list
    """
    syms = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    num = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
    x = syms[param1[0]]
    y = num[param1[1]]
    xx = syms[param2[0]]
    xy = num[param2[1]]

    if xx == x - 1 and xy == y + 1 or xy == y - 1:

        return [x, y], [xx, xy]

    elif xx == x - 2 and xy == y + 2 or xy == y - 2:

        return [x, y], [xx, xy]
    else:
        print ("Checkers go only diagonally, repeat the selection")


def print_deck (player_checkers,bot_checkers, deck):
    """
    This function prints a checker board
    :param player_checkers: list of player checkers coordinates
    :param bot_checkers: list of coordinates of bot checkers
    :param deck: playing field
    :type player_checkers: list
    :type bot_checkers:   list
    :type deck:   list
    :return: checkered field
    :rtype:   list
    """
    res = "   1  2  3  4  5  6  7  8" + "\n"
    alfa = ["A ", "B ", "C ", "D ", "E ", "F ", "G ", "H "]

    for i in player_checkers:
        deck[i[0]][i[1]] = "|X|"

    for j in bot_checkers:
        deck[j[0]][j[1]] = "|O|"

    for i in range(8):
        res += alfa[i] + "".join( deck[i]) + "\n"

    print(res)


def bot_move(player_checkers, bot_checkers):
    """
    This function is responsible for the logic of the bot
    :param player_checkers: list of player checkers coordinates
    :param bot_checkers: list of coordinates of bot checkers
    :type player_checkers: list
    :type bot_checkers:   list
    :return: travel coordinates
    :rtype:   list
    """

    bot_step = []
    bot_beat = []


    for i in bot_checkers:

        new_elements = [[i[0]+1, i[1]+1], [i[0]+1, i[1]-1], [i[0]-1, i[1]+1], [i[0]-1, i[1]-1]]

        for j in new_elements:
            if j in player_checkers:

                bot_beat.append(j)

    for x in bot_beat:
        new_step = [x[0]-1, x[1]+1], [x[0]+1, x[1]-1],

        for y in new_step:
            if y not in bot_step and y not in player_checkers and y not in bot_checkers and y[0] <= 7 and y[1] >= 0:
                bot_step.append(y)

    #for v in bot_step:
        #old_checker = [v[0] - 1][v[1] + 1], [v[0] + 1][v[1] - 1]

        #for t in old_checker:

            #if t in player_checkers:
               # print (t, "t")

            #deck[v[0]][v[1]] = "|O|"

            #if old_checker in player_checkers:
            #deck[v[0]-1][v[1]-1] = "|Y|"
            #index_checker = player_checkers.index(player_checkers[v[0]+1][v[1]-1])

            #deck[bot_checkers[index_checker][0]][bot_checkers[index_checker][1]] = "|_|"
            #player_checkers.pop(index_checker)

    len_bot_step = len(bot_beat)

    if len_bot_step == 0:
        bot_moves = []

        while True:
            i = random.choice(bot_checkers)
            new_elements = [[i[0] + 1, i[1] + 1], [i[0] + 1, i[1] - 1], [i[0] - 1, i[1] + 1], [i[0] - 1, i[1] - 1]]
            for j in new_elements:
                if j not in player_checkers and j not in bot_checkers and j[0] < 7 and j[0] >= 0 and j[1] >= 0 and j[1] < 7:
                    bot_moves.append(j)
            break

    print("bot_moves")



player_checkers = [[5, 0], [5, 2], [5, 4], [5, 6], [6, 1], [6, 3], [6, 5], [6, 7], [7, 0], [7, 2], [7, 4], [7, 6]]
bot_checkers = [[0, 1], [0, 3], [0, 5], [0, 7], [1, 0], [1, 2], [1, 4], [1, 6], [2, 1], [2, 3], [2, 5], [2, 7]]
deck = [["|_|", ] * 8 for i in range(8)]

while True:

    player_choise = input("What color do you want to play? white or black ")

    if player_choise.lower() == "black":
        bot_move(player_checkers, bot_checkers)
        break
    elif player_choise.lower() == "white":
        break
    else:
        print("repeat your choice")

while True:

    player_len = len(player_checkers)
    bot_len = len(bot_checkers)

    if bot_len == 0:

        print("You winer")
        break

    elif player_len == 0:

        print("You lose")
        break

    print_deck(player_checkers, bot_checkers, deck)
    player_move = input("do you move or beat the enemy? ")

    if player_move.lower() == "move":

        checkers_selection = input("what checker do you want to move ")
        checkers_move = input("where do you want to move ")
        coord_move = coordin(checkers_selection.upper(), checkers_move.upper())
        move = list(coord_move)

        if move[0] in player_checkers and deck[move[1][0]][move[1][1]] == "|_|":

            index_element = player_checkers.index(move[0])
            player_checkers[index_element] = move[1]
            deck[move[0][0]][move[0][1]] = "|_|"

        else:
            print("repeat your choice")


    elif player_move.lower() == "beat":

        checkers_selection = input("what checker do you want to move ")
        checkers_beat = input("which checker do you want to beat ")
        coord_beat = coordin(checkers_selection.upper(), checkers_beat.upper())
        beat = list(coord_beat)
        new_element = list([beat[0][0] - 1, beat[0][1] - 1])
        new_element2 = [beat[0][0] - 1, beat[0][1] + 1]

        if new_element2 in bot_checkers:
            new_element = list(new_element2)

        if beat[0] in player_checkers and deck[beat[1][0]][beat[1][1]] == "|_|" and new_element in bot_checkers:

            index_element = player_checkers.index(beat[0])
            player_checkers[index_element] = beat[1]
            deck[beat[0][0]][beat[0][1]] = "|_|"
            index_checker = bot_checkers.index(new_element)
            deck[bot_checkers[index_checker][0]][bot_checkers[index_checker][1]] = "|_|"
            bot_checkers.pop(index_checker)

        else:

            print("repeat your choice")
    bot_move(player_checkers, bot_checkers)

