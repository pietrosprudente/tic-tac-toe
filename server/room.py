from game import Game
from player import Player


class Room:
    def __init__(self, _code, _status):
        self.code = _code
        self.status = _status
        self.hostPlayer = (Player);
        self.guestPlayer = (Player)
        self.game = Game()

    def getOppositePlayer(self, connection):
        if self.hostPlayer != connection:
            return self.guestPlayer;
        else: 
            return self.hostPlayer;

    def getPlayer(self, connection):
        if self.hostPlayer.connection == connection:
            return self.hostPlayer;
        else:
            return self.guestPlayer;