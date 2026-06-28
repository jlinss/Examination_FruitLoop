from src.grid import Grid
from src.player import Player
from src import pickups

class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):
        self.player = Player(17,6) # (Krav 1 - Spelaren "@" ska börja nära mitten): 17 - 6 är ungefär mitten av spelet.
        #self.player = Player(2, 1)
        self.score = 0
        self.inventory = []

        self.g = Grid()
        self.g.set_player(self.player)
        self.g.make_walls()
        pickups.randomize(self.g)
