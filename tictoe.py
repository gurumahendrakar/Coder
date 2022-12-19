
class tictoe:

    def __init__(self):
        self.__list = ['0'  for  x in range(9) ]
        self.player_chooser = False
        self.winner  = False


    def play_show(self):

        print(('------------------'))
        print('       '.join(self.__list[:3]))
        print(('------------------'))
        print('       '.join(self.__list[3:6]))
        print('------------------')
        print('       '.join((self.__list[6:])))
        print(('------------------'))

    def __computer(self):
        import random

        number_slot = random.choice([index for index,x in enumerate(self.__list) if x !='❂' and x !='₪'])

        print('Computer Choice : ',number_slot)
        self.__list[number_slot] = '₪'


    def player(self):

        while not self.player_chooser:

            if self.player_chooser == False:
                print()
                self.play_show()
                print()


            __main__ = int(input(' Please Choose  !!  >>>'))

            if __main__>8: continue

            else:

                if self.__list[__main__] != '₪' and self.__list[__main__]!='❂':
                    self.player_chooser = True
                    self.__list[__main__] = '❂'

                else:

                    avilabels_moves = '|'.join([str(index) for index,x in enumerate(self.__list) if x != '❂' and x!='₪'])

                    print('----THIS IS ALREADY FILLED YOU CAN CHOOSE-----\n Not Filled : {}'.format(avilabels_moves))
        else:
            self.player_chooser = False


    def winning_checker(self):


        for a,b,c in ([[0,1,2],[3,4,5],[6,7,8]]):
            if self.__list[a]==self.__list[b]==self.__list[c] and self.__list[a] != '0':

                self.winner = self.__list[a]
                break

        for a, b, c in ([[0,4,8], [2,4,6]]):
            if self.__list[a] == self.__list[b] == self.__list[c] and self.__list[a] != '0':
                self.winner = self.__list[a]
                break

        for a, b, c in ([[0,3,6], [1,4,7], [2,5,8]]):
            if self.__list[a] == self.__list[b] == self.__list[c] and self.__list[a] != '0':
                self.winner = self.__list[a]
                break

    def __mainboard__(self):

        while not self.winner:
           self.__computer()
           self.winning_checker()
           if not self.winner:
               self.player()

        else:
            self.play_show()
            print('Winner >> ',self.winner)

            if input(' If You Want to Play Press Anything!!\n'
                               'Do You Want Not Play Press Enter 2 Times !!'):
                self.__list = ['0' for x in range(9)]
                self.winner = None
                self.__mainboard__()



tO = tictoe()
tO.__mainboard__()
