
class Item:
    """Representerar saker man kan plocka upp."""
    #def __init__(self, name, value=10, symbol="?"):
    def __init__(self, name, value=20, symbol="?"): #Frukter värdar 20 poäng nu
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball")]


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

# Här var lagt fällor till spelaren
class Trap:
    """Fällor som gör man förlora 10 poäng"""
    def __init__(self):
        self.symbol = "T"

    def __str__(self):
        return self.symbol

def randomize_trap(grid):
        for i in range(5):
            while True:
                x = grid.get_random_x()
                y = grid.get_random_y()

                if grid.is_empty(x,y):
                    grid.set(x,y, Trap())
                    break
