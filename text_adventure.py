class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}   # filled in after all rooms are created, see main()
        self.items = []


class Player:
    def __init__(self, current_room, health):
        self.current_room = current_room
        self.inventory = []
        self.health = health


def print_room(room):
    """Shared by the main loop and the 'look' command so both show the
    same room info without duplicating the print statements."""
    print(f"\n{room.name}")
    print(room.description)
    print("Exits:", ", ".join(room.exits.keys()))


def main():
    hallway = Room("Hallway", "A dim hallway with peeling wallpaper.")
    kitchen = Room("Kitchen", "A dusty kitchen, pots hanging from the ceiling.")
    library = Room("Library", "Shelves of old books line the walls.")
    cellar = Room("Cellar", "A cold, damp cellar. It smells like earth.")

    # Rooms need to exist before they can reference each other, so exits
    # are assigned after all four Room objects are created, not inside
    # Room.__init__.
    hallway.exits = {"north": kitchen, "east": library}
    kitchen.exits = {"south": hallway, "down": cellar}
    library.exits = {"west": hallway}
    cellar.exits = {"up": kitchen}

    hallway.items = ["lantern"]
    kitchen.items = ["knife", "bread"]
    library.items = ["old book"]
    cellar.items = ["rusty key"]

    player = Player(hallway, 100)

    while True:
        print_room(player.current_room)

        command = input("\nWhat do you do? ")
        words = command.lower().split()

        if len(words) == 0:
            print("Please type a command.")
            continue

        action = words[0]

        if action == "go":
            if len(words) < 2:
                print("Go where?")
                continue
            direction = words[1]
            if direction in player.current_room.exits:
                player.current_room = player.current_room.exits[direction]
                if player.current_room.name == "Cellar":
                    print("Congrats! You have won the game!")
                    break
                elif player.current_room.name == "Library":
                    player.health -= 25
                    print(f"Your health decreased by 25 points! it is now {player.health}")
                    if player.health <= 0:
                        print("You are dead and have lost the game!")
                        break
            else:
                print("You can't go that way.")

        elif action == "take":
            if len(words) < 2:
                print("Take what?")
                continue
            item = words[1]
            if item in player.current_room.items:
                player.current_room.items.remove(item)
                player.inventory.append(item)
                print(f"You took {item}!")
            else:
                print("There is no such item in this room")

        elif action == "look":
            print_room(player.current_room)

        elif action == "inventory":
            if len(player.inventory) >= 1:
                for n, item in enumerate(player.inventory, start=1):
                    print(f"Item {n}:", item)
            else:
                print("No items in your inventory.")

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()