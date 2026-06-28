from src import pickups
from src.status import print_status
from src.game_state import GameState

def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)

        command = input("Use WASD to move, Q/X to quit. ")
        command = command.casefold()[:1]

        # här finns hur varje bokstav ska röra sig
        if command == "w":
            move_player(state, dx=0, dy=-1)

        elif command == "a":
            move_player(state, dx=-1, dy=0)

        elif command == "s":
            move_player(state, dx=0, dy=1)

        elif command == "d":
            move_player(state, dx=1, dy=0)

        elif command == "i": # Kommandot "i" som ska visa vad spelare har i inventory
            print("Inventory:")

            if len(state.inventory) == 0:
                print("Empty Inventory")

            else:
                for item in state.inventory:
                    print("-", item)

    # Hit kommer vi när while-loopen slutar
    print("Thank you for playing!")

def move_player(state, dx, dy): # Funktionen ska möjliggöra spelaren röra sig med WASD
    if state.player.can_move(dx, dy, state.g):
        maybe_item = state.g.get(state.player.pos_x + dx, state.player.pos_y + dy)
        state.player.move(dx,dy)
        state.score -= 1 #Lava

        if isinstance(maybe_item, pickups.Item):
            state.score += maybe_item.value
            state.inventory.append(maybe_item.name) #Lägg till i listan allt som vi plockar upp

            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            state.g.clear(state.player.pos_x, state.player.pos_y)

        if isinstance(maybe_item, pickups.Trap):
            state.score -= 10
            print("You found a trap, -10 points.")

# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)