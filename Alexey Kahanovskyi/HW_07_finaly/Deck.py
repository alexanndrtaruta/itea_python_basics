import random

class Main:

    def __init__(self):

        self._x = 'x'
        self._o = 'o'
        self.desk_list = [['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                          [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                          ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                          ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
                          [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o']]

    def print_list(self):

        """
        Function for printing playing field for checkers
        """

        print('  A ', ' B ', ' C ', ' D ', ' E ', ' F ', ' G ', ' H ')

        for i in self.desk_list:

            for j in range(1):
                print('|', ' | '.join(i), '|')


    def count_check(self):

        """
        Function for counting the number of game checkers
        :return: True (if number of game checkers both teams > 0) or False(  if number of game checkers any teams = 0)
        :rtype: bool
        """

        self.count_x = []
        self.count_o = []

        for k in range(len(self.desk_list)):
            for l in range(8):

                if self.desk_list[k][l] == 'x':
                    self.count_x.append(l)

                elif self.desk_list[k][l] == 'o':
                    self.count_o.append(l)

        print('x count = ', len(self.count_x))
        print('o count = ', len(self.count_o))

        if len(self.count_x) != 0 and len(self.count_o) != 0:
            return True


    def new_index(self):

        """
        Function for converting desk_list's indeces in new indeces (letter and number)
        """

        index_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        new_index_list = [0, 1, 2, 3, 4, 5, 6, 7]

        self.di = dict(zip(index_list, new_index_list))

        self.j = self.di[input('letter : ')]
        self.i = (int(input('i = ')) - 1)


    def cord(self):

        """
        Function for creating lists of coordinates of x, o, empty cells and lists and lists of coordinates of nearby cells
        :return: lists of coordinates of x, o, empty cells and lists and lists of coordinates of nearby cells
        :rtype: list
        """

        desk_list = self.desk_list

        self.x = []
        self.o = []
        self.noth = []

        for i in range(len(desk_list)):
            for j in range(len(desk_list[i])):

                if desk_list[i][j] == 'x':
                    self.x.append([i, j])

                elif desk_list[i][j] == 'o':
                    self.o.append([i, j])

                else:
                    self.noth.append([i, j])

        self.pkus_x = [[l + 1, j + 1] for l, j in self.x] #lists for mooving x
        self.pkus_2 = [[l + 1, j - 1] for l, j in self.x]
        self.pkus_3 = [[l - 1, j + 1] for l, j in self.x]
        self.pkus_4 = [[l - 1, j - 1] for l, j in self.x]

        self.pkus_o1 = [[l + 1, j + 1] for l, j in self.o]#lists for mooving o
        self.pkus_o2 = [[l + 1, j - 1] for l, j in self.o]
        self.pkus_o3 = [[l - 1, j + 1] for l, j in self.o]
        self.pkus_o4 = [[l - 1, j - 1] for l, j in self.o]

        self.pkus_o2_1 = [[l + 2, j + 2] for l, j in self.o]#lists for fighting o
        self.pkus_o2_2 = [[l + 2, j - 2] for l, j in self.o]
        self.pkus_o2_3 = [[l - 2, j + 2] for l, j in self.o]
        self.pkus_o2_4 = [[l - 2, j - 2] for l, j in self.o]

        self.pkus_1 =self.pkus_x + self.pkus_2 #for possibilities to moove team x
        self.pkus_for_def_fight = self.pkus_x + self.pkus_2 + self.pkus_3 + self.pkus_4 #for possibilities to fight vs bot for team x

        self.pkus_o = self.pkus_o3 + self.pkus_o4#for possibilities to moove team x
        self.pkus_for_bot = self.pkus_o1 + self.pkus_o2 + self.pkus_o3 + self.pkus_o4#for possibilities to fight vs bot for team o
        self.pkus_o2_com = self.pkus_o2_1 + self.pkus_o2_2 + self.pkus_o2_3 + self.pkus_o2_4#for possibilities to fight vs bot for team o
        return(self.x, self.o, self.noth, self.pkus_1,self.pkus_for_def_fight,self.pkus_for_bot, self.pkus_o)


    def checker_moove(self):

        """
        Function for checking mooving possibilities of Player and move his checkers
        """

        self.ind = []

        for a in range(len(self.pkus_1)):
            for b in range(len(self.noth)):

                if self.pkus_1[a] == self.noth[b]:

                    self.ind.append(self.pkus_1[a])# possible moves

        for x in range(len(self.ind)):

            self.ch_l = self.di[input(' Enter index of your tern : (letter) : ')]
            self.ch_n = int(input(' Enter index of your tern : (num) : ')) - 1

            if [self.ch_n, self.ch_l] == self.ind[x]:

                self.desk_list[self.ch_n][self.ch_l] = self.desk_list[self.i][self.j]
                self.desk_list[self.i][self.j] = ' '
                break


    def fight_vs_bot(self):

        """
        Function for checking fighting possibilities vs bot and fight
        """

        self.indy = []
        self.fght = []# possible variants to moove to beat the bot's checker

        for i in range(len(self.pkus_for_def_fight)):
            for j in range(len(self.o)):

                if self.pkus_for_def_fight[i] == self.o[j]:
                    self.indy.append(self.pkus_for_def_fight[i])

        self.indy = sorted(self.indy)
        self.sort_indy = [self.indy[i] for i in range(len(self.indy)) if i == 0 or self.indy[i] != self.indy[i - 1]]# шашки по диaгонали от моих х

        self.indy_plus_1 = [[l + 1, j + 1] for l, j in self.sort_indy]
        self.indy_plus_2 = [[l + 1, j - 1] for l, j in self.sort_indy]
        self.indy_plus_3 = [[l - 1, j + 1] for l, j in self.sort_indy]
        self.indy_plus_4 = [[l - 1, j - 1] for l, j in self.sort_indy]

        self.indy_common = self.indy_plus_1 + self.indy_plus_2 + self.indy_plus_3 + self.indy_plus_4

        for x in range(len(self.indy_common)):
            for y in range(len(self.noth)):

                if self.indy_common[x] == self.noth[y]:

                    self.fght.append(self.indy_common[x])

        self.ch_l_f = self.di[input(' Enter index of your tern : (letter) : ')]
        self.ch_n_f = int(input(' Enter index of your tern : (num) : ')) - 1

        for x in range(len(self.sort_indy)):

            if [self.ch_n_f - 1, self.ch_l_f - 1] == self.sort_indy[x]  :


                self.desk_list[self.ch_n_f][self.ch_l_f] = self.desk_list[self.i][self.j]
                self.desk_list[self.i][self.j] = ' '
                self.desk_list[self.ch_n_f - 1][self.ch_l_f - 1] = ' '
                break

            elif [self.ch_n_f + 1, self.ch_l_f - 1] == self.sort_indy[x]:

                self.desk_list[self.ch_n_f][self.ch_l_f] = self.desk_list[self.i][self.j]
                self.desk_list[self.i][self.j] = ' '
                self.desk_list[self.ch_n_f + 1][self.ch_l_f - 1] = ' '
                break

            elif [self.ch_n_f - 1, self.ch_l_f + 1] == self.sort_indy[x]:

                self.desk_list[self.ch_n_f][self.ch_l_f] = self.desk_list[self.i][self.j]
                self.desk_list[self.i][self.j] = ' '
                self.desk_list[self.ch_n_f - 1][self.ch_l_f + 1] = ' '
                break

            elif [self.ch_n_f + 1, self.ch_l_f + 1] == self.sort_indy[x] :

                self.desk_list[self.ch_n_f][self.ch_l_f] = self.desk_list[self.i][self.j]
                self.desk_list[self.i][self.j] = ' '
                self.desk_list[self.ch_n_f + 1][self.ch_l_f + 1] = ' '
                break


    def bot_moove(self):

        """
        Function for checking mooving possibilities of Bot and move his checkers
        """

        self.ind_bot = []

        for a in range(len(self.pkus_o)):
            for b in range(len(self.noth)):

                if self.pkus_o[a] == self.noth[b]:

                    self.ind_bot.append(self.pkus_o[a])

        self.i_bot, self.j_bot = random.choice(self.ind_bot)[0], random.choice(self.ind_bot)[1]

        for x in range(len(self.o)):

            if [self.i_bot + 1, self.j_bot - 1] == self.o[x] :

                self.desk_list[self.i_bot][self.j_bot] = self.desk_list[self.i_bot + 1][self.j_bot - 1]
                self.desk_list[self.i_bot + 1][self.j_bot - 1] = ' '
                break

            elif [self.i_bot + 1, self.j_bot + 1] == self.o[x]:

                self.desk_list[self.i_bot][self.j_bot] = self.desk_list[self.i_bot + 1][self.j_bot + 1]
                self.desk_list[self.i_bot + 1][self.j_bot + 1] = ' '
                break

            else:
                print(" You can't moove")


    def bot_fight_checker(self):

        """
        Function checking fight possibility
        """

        for i in range(len(self.pkus_for_bot)):
            for j in range(len(self.x)):
                for k in range(len(self.noth)):
                    for z in range(len(self.pkus_o2_com)):

                        if self.pkus_for_bot[i] == self.x[j] and self.pkus_o2_com[z] == self.noth[k]:

                            return(True)


    def bot_fight(self):

        """
        Function for beat Player's checker
        """

        self.indy_bot_f = []
        self.fght_bot = []

        for i in range(len(self.pkus_for_bot)):
            for j in range(len(self.x)):

                if self.pkus_for_bot[i] == self.x[j]:

                    self.indy_bot_f.append(self.pkus_for_bot[i])


        self.indy_bot_f = sorted(self.indy_bot_f)
        self.sort_indy_bot_f = [self.indy_bot_f[i] for i in range(len(self.indy_bot_f)) if i == 0 or self.indy_bot_f[i] != self.indy_bot_f[i - 1]]

        self.indy_b_plus_1 = [[l + 1, j + 1] for l, j in self.sort_indy_bot_f]
        self.indy_b_plus_2 = [[l + 1, j - 1] for l, j in self.sort_indy_bot_f]
        self.indy_b_plus_3 = [[l - 1, j + 1] for l, j in self.sort_indy_bot_f]
        self.indy_b_plus_4 = [[l - 1, j - 1] for l, j in self.sort_indy_bot_f]

        self.indy_common_b = self.indy_b_plus_1 + self.indy_b_plus_2 + self.indy_b_plus_3 + self.indy_b_plus_4

        for x in range(len(self.indy_common_b)):
            for y in range(len(self.noth)):

                if self.indy_common_b[x] == self.noth[y]:
                    self.fght_bot.append(self.indy_common_b[x])

        self.i_bot, self.j_bot = random.choice(self.fght_bot)[0], random.choice(self.fght_bot)[1]

        for x in range(len(self.indy_bot_f)):

            if [self.i_bot + 1, self.j_bot + 1] == self.indy_bot_f[x] and self.i_bot != 6 and self.i_bot != 7:

                self.desk_list[self.i_bot][self.j_bot] = self.desk_list[self.i_bot + 2][self.j_bot + 2]
                self.desk_list[self.i_bot + 2][self.j_bot + 2] = ' '
                self.desk_list[self.i_bot + 1][self.j_bot + 1] = ' '

                break

            elif [self.i_bot + 1, self.j_bot - 1] == self.indy_bot_f[x] and self.i_bot != 0 and self.i_bot != 1:

                self.desk_list[self.i_bot][self.j_bot] = self.desk_list[self.i_bot + 2][self.j_bot - 2]
                self.desk_list[self.i_bot + 2][self.j_bot - 2] = ' '
                self.desk_list[self.i_bot + 1][self.j_bot - 1] = ' '

                break

            elif [self.i_bot - 1, self.j_bot + 1] == self.indy_bot_f[x]:

                self.desk_list[self.i_bot][self.j_bot] = self.desk_list[self.i_bot - 2][self.j_bot + 2]
                self.desk_list[self.i_bot - 2][self.j_bot + 2] = ' '
                self.desk_list[self.i_bot - 1][self.j_bot + 1] = ' '

                break

            elif [self.i_bot - 1, self.j_bot - 1] == self.indy_bot_f[x]:

                self.desk_list[self.i_bot][self.j_bot] = self.desk_list[self.i_bot - 2][self.j_bot - 2]
                self.desk_list[self.i_bot - 2][self.j_bot - 2] = ' '
                self.desk_list[self.i_bot - 1][self.j_bot - 1] = ' '

                break

