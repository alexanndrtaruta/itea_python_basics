
class Deck:

    white_player = 1
    black_player = 0

    width = 8
    height = 8
    undone_step = -1

    def __init__(self, whoFirst = 0):
        self.width = self.width
        self.height = self.height

        self.black_matrix = []
        self.white_matrix = []
    
        for i in range(self.width):
            self.black_matrix.append((i, (i + 1) % 2))
            self.white_matrix.append((i, self.height - (i % 2) - 1))

        self.alignment = [[' '] * self.width for x in range(self.height)]
        self.win_status = self.undone_step
        self.turn = whoFirst
        self.maximum = 10

    def generate_white_moves(self):
        for part in self.white_matrix:
            for step in self.generate(part, ((-1, -1), (1, -1))):
                yield step

    def generate_black_movements(self):
        for part in self.black_matrix:
            for step in self.generate(part, ((-1, 1), (1, 1))):
                yield step


    def generate(self, part, steps):
        
        for step in steps:
            x = part[0] + step[0]
            y = part[1] + step[1]

            if (x < 0 or x >= self.width) or (y < 0 or y >= self.height): #parentheses for readability purposes...
                continue
            
            coordinates = (x, y) #combine this tuple into the variable

            #Verifying whether there are no any barriers in front of unit moving...
            black = coordinates in self.black_matrix
            white = coordinates in self.white_matrix

            if not black and not white:
                yield(part, coordinates, self.undone_step)
            else:
                #Here we're going to decide if it'll be possible to jump through the unit
                if self.turn == self.black_player and black: #it should be the different color unit to jump through it
                    continue
                elif self.turn == self.white_player and white:
                    continue
                
                step_into_x = coordinates[0] + step[0] # just(x)
                step_into_y = coordinates[1] + step[0] # just(y)

                #Skip the jump if it goes to far...
                if step_into_x < 0 or step_into_x >= self.width or step_into_y < 0 or step_into_y >= self.height:
                    continue
                
                jump_coordinates = (step_into_x, step_into_y) #save the jumping coordinate tuple into the variable...

                #Verifying if there's an empty space where to jump to...
                black = jump_coordinates in self.black_matrix
                white = jump_coordinates in self.white_matrix

                if not black and not white:
                    yield(part, jump_coordinates, self.turn)


    def redraw_deck(self):
        for i in range(self.width): #assign the list to empty spaces
            for j in range(self.height):
                self.alignment[i][j] = " "

        #fill the black matrix
        for black in self.black_matrix:
            x = black[1]
            y = black[0]
            self.alignment[x][y] = "x" # x - is the black player

        #fill the white matrix
        for white in self.white_matrix:
            x = white[1]
            y = white[0]
            self.alignment[x][y] = "o" # o - is the white player

    def move_black(self, start, finish, winner):
        self.black_move_handler(start, finish, winner)
        self.redraw_the_game()

    def move_white(self, start, finish, winner):
        self.white_move_handler(start, finish, winner)
        self.redraw_the_game()


    def black_move_handler(self, start, finish, winner):
        
        if (finish[0] < 0 or finish[0] >= self.width) or (finish[1] < 0 or finish[1] >= self.height):
            raise Exception("Movement is out of bound for black player")
        
        black = finish in self.black_matrix
        white = finish in self.white_matrix

        if not (black or white):
            self.black_matrix[self.black_matrix.index(start)] = finish
            self.redraw_deck()
            self.turn = self.white_player
            self.win_status = winner
        else:
            raise Exception

    
    def white_move_handler(self, start, finish, winner):
        
        if (finish[0] < 0 or finish[0] >= self.width) or (finish[1] < 0 or finish[1] >= self.height):
            raise Exception("Movement if out of bound for white player")
        
        black = finish in self.black_matrix
        white = finish in self.white_matrix

        if not (black or white):
            self.white_matrix[self.white_matrix.index(start)] = finish
            self.redraw_deck()
            self.turn = self.black_player
            self.win_status = winner
        else:
            Exception

    def redraw_the_game(self):
        print(self.__unicode__())

    def __unicode__(self):
        self.redraw_deck()
        vectors = []
        # This prints the numbers at the top of the Game Board
        vectors.append('    ' + '   '.join(map(str, range(self.width))))
        # Prints the top of the gameboard in unicode
        vectors.append(u'  ╭' + (u'───┬' * (self.width-1)) + u'───╮')
        
        # Print the boards rows
        for num, row in enumerate(self.alignment[:-1]):
            vectors.append(chr(num+65) + u' │ ' + u' │ '.join(row) + u' │')
            vectors.append(u'  ├' + (u'───┼' * (self.width-1)) + u'───┤')
        
        #Print the last row
        vectors.append(chr(self.height+64) + u' │ ' + u' │ '.join(self.alignment[-1]) + u' │')

        # Prints the final line in the board
        vectors.append(u'  ╰' + (u'───┴' * (self.width-1)) + u'───╯')
        return '\n'.join(vectors)

