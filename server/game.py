class Game:
    #board state = represented by bytes with 0 = empty, 1 = X, 2 = O
    def __init__(self):
        self.board = [0, 0, 0, 
                       0, 0, 0, 
                       0, 0, 0]
        self.turn = 1