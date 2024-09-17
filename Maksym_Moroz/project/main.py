import random
import deck_objects

variants = ["x", "o"]
player_chacker = random.choice(variants)

bot_chacker = [i for i in variants if i != player_chacker]
print(bot_chacker)

if player_chacker == "x":
    print(f"You will play {player_chacker} (black)")
    play_deck = deck_objects.Deck()
    play_deck.revers()


else:
    print(f"You will play {player_chacker} (white)")
    play_deck = deck_objects.Deck()


play_deck.print_deck()

while True:


    input_turn = input("Your turn\n")
    input_turn = input_turn.lower()

    coord_tuple = play_deck.convert_input_to_coord(input_turn)

    print(type(coord_tuple))
    print(coord_tuple)

    print(play_deck)

    turn_checker = play_deck.deck[coord_tuple[0]][coord_tuple[1]]

    print(turn_checker)

    if play_deck.deck[coord_tuple[0]][coord_tuple[1]] != " " and play_deck.deck[coord_tuple[0]][coord_tuple[1]] != bot_chacker[0] and (play_deck.deck[coord_tuple[0] + 1][coord_tuple[1] + 1] == " " or play_deck.deck[coord_tuple[0] + 1][coord_tuple[1] - 1] == " "):
        print("You can turn")

        input_turn2 = input("What Youe step\n")
        c = play_deck.convert_input_to_coord(input_turn2)
        print(c)
        d = play_deck.deck[c[0]][c[1]]
        l1 = play_deck.deck[0][c[1] + 1]
        l1 = l1.lower()
        m1 = play_deck.deck[0][c[1] - 1]
        m1 = m1.lower()
        print(l1)
        print(m1)

        if d == player_chacker:
            print("fuck2")

  #      if (input_turn2[0] != l1 and input_turn2[0] != m1) and (input_turn2[0] == input_turn[0] or int(input_turn2[1]) <= int(input_turn[1]) or (int(input_turn2[1]) - int(input_turn[1])) != 1):
        elif (int(input_turn2[1]) - int(input_turn[1])) == 1 and (input_turn[0] == l1 or input_turn[0] == m1):

            play_deck.deck[c[0]][c[1]] = turn_checker
            play_deck.deck[coord_tuple[0]][coord_tuple[1]] = " "
            print(play_deck.deck[c[0]][c[1]])

        else:
            print("fuck")
            print(l1)
            print(m1)
            print(input_turn2[0])



    elif (play_deck.deck[coord_tuple[0] + 1][coord_tuple[1] + 1] == bot_chacker[0] and play_deck.deck[coord_tuple[0] + 2][coord_tuple[1] + 2] == " ") or (play_deck.deck[coord_tuple[0] - 1][coord_tuple[1] - 1] == bot_chacker[0] and play_deck.deck[coord_tuple[0] - 2][coord_tuple[1] - 2] == " ") or (play_deck.deck[coord_tuple[0] - 1][coord_tuple[1] + 1] == bot_chacker[0] and play_deck.deck[coord_tuple[0] - 2][coord_tuple[1] + 2] == " ") or (play_deck.deck[coord_tuple[0] + 1][coord_tuple[1] - 1] == bot_chacker[0] and play_deck.deck[coord_tuple[0] + 2][coord_tuple[1] - 2] == " "):
           # or play_deck.deck[coord_tuple[0] + - 1][coord_tuple[1] + - 1] == bot_chacker[0]
        print("You can attack")
        input_turn2 = input("What Youe step\n")
        attack_coord = play_deck.convert_input_to_coord(input_turn2)
        print(attack_coord)
        attack_checker = play_deck.deck[attack_coord[0]][attack_coord[1]]
        print(attack_checker)

        if attack_coord[1] > coord_tuple[1] and attack_coord[0] > coord_tuple[0]:
            play_deck.deck[attack_coord[0] - 1][attack_coord[1] - 1] = " "
            play_deck.deck[attack_coord[0]][attack_coord[1]] = play_deck.deck[coord_tuple[0]][coord_tuple[1]]
            play_deck.deck[coord_tuple[0]][coord_tuple[1]] = " "


        if attack_coord[1] < coord_tuple[1] and attack_coord[0] > coord_tuple[0]:

            play_deck.deck[attack_coord[0] - 1][attack_coord[1] + 1] = " "
            play_deck.deck[attack_coord[0]][attack_coord[1]] = play_deck.deck[coord_tuple[0]][coord_tuple[1]]
            play_deck.deck[coord_tuple[0]][coord_tuple[1]] = " "

        if attack_coord[1] > coord_tuple[1] and attack_coord[0] < coord_tuple[0]:

            play_deck.deck[attack_coord[0] + 1][attack_coord[1] - 1] = " "
            play_deck.deck[attack_coord[0]][attack_coord[1]] = play_deck.deck[coord_tuple[0]][coord_tuple[1]]
            play_deck.deck[coord_tuple[0]][coord_tuple[1]] = " "

        if attack_coord[1] < coord_tuple[1] and attack_coord[0] < coord_tuple[0]:


            play_deck.deck[attack_coord[0] + 1][attack_coord[1] + 1] = " "
            play_deck.deck[attack_coord[0]][attack_coord[1]] = play_deck.deck[coord_tuple[0]][coord_tuple[1]]
            play_deck.deck[coord_tuple[0]][coord_tuple[1]] = " "

    else:
        print("Turn yet")


    play_deck.print_deck()

    print(play_deck.move_bot(bot_chacker[0]))
    play_deck.print_deck()








