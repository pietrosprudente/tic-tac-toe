class Room:
    def __init__(self, _code, _status):
        self.code = _code
        self.status = _status
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)