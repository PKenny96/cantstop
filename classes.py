class Player:
    """Player class inputs are normally game piece marker (a character) and score
    """
    def __init__(self, piece, score):
        self.name = None
        self.piece = piece
        self.score = score



class Gameboard:

    def __init__(self, player_list):
        self.board = [["","",""],
                      ["","","","",""],
                      ["","","","","","",""],
                      ["","","","","","","","",""],
                      ["","","","","","","","","","",""],
                      ["","","","","","","","","","","","",""],
                      ["","","","","","","","","","",""],
                      ["","","","","","","","",""],
                      ["","","","","","",""],
                      ["","","","",""],
                      ["","",""],  
                     ]

        self.players = player_list

    def __str__(self):
        for player in self.player_list:
            print("{}: {}".format(player.piece, player.score))

        for line in range(len(self.board)):
            for pos in self.board[line]:
                if pos == "":
                    print("0", end = "-")

                else:
                    print(pos, end = "-")

            print(line+2)














                
