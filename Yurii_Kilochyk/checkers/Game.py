from pprint import PrettyPrinter
from Desk import Deck

class Game:

    def define_winner(self, deck: Deck): return deck.win_status or deck.undone_step

    def retrieve_current_user_move(self, deck: Deck):
        welcome_message = "Enter start coordinate and where to move coordinate (e.g. G1 F0):"
        print(welcome_message)

        while True:
            step = []
            step = input().lower().split()

            if not (len(step) == 2): #should be two chars
                print("Cannot doing steps like this. \n" + welcome_message)
                continue
            
            step_from_up = (int(step[0][1]), ord(step[0][0]) - 97)
            step_to_up = (int(step[1][1]), ord(step[1][0]) - 97)

            if not step_from_up in deck.white_matrix:
                print("Sorry, you haven't got this one!")
                continue
            break
        
        step = (step_from_up, step_to_up, deck.undone_step)
        
        return step

    def initialize(self):
        deck = Deck()
        deck.redraw_the_game()

        print("* * * WELCOME TO MY CHECKERS GAME! * * *")

        while deck.win_status == -1:
            step = self.retrieve_current_user_move(deck)

            try:
                deck.move_white(*step)
            except Exception:
                print("Incorrect step")
                continue
            
            print("It is the BOT turn!")
            deck.redraw_deck()

            if deck.win_status == deck.white_player:
                print("WHITE PLAYER IS THE WINNER!")
            elif deck.win_status == deck.black_player:
                print("BLACK PLAYER IS THE WINNER!")
                break





