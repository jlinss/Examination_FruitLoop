class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    # def can_move(self, x, y, grid):
    #     return True
    #     #TODO: returnera True om det inte står något i vägen

    def can_move(self, dx, dy, grid): #Här ska vi inte möjliggöra player gå igenom väggar
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy

        return grid.get(new_x, new_y) != grid.wall
