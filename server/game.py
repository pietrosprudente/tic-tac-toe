class Game:
    #board state = represented by bytes with 0 = empty, 1 = X, 2 = O
    def __init__(self):
        self.board = [0, 0, 0, 
                       0, 0, 0, 
                       0, 0, 0]
        self.turn = 1

    def placeMark(self, player, spot):
        if(self.canPlay(player)):
            self.board[spot] = player
            if self.turn == 1:
                self.turn = 2;
            else:
                self.turn = 1;
    
    def canPlay(self, turn):
        return turn == self.turn;