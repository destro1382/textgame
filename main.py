print("Welcome to Drantill")
from player import Player
from rooms import all_rooms

def main():
    player_name = input("What is your name, adventurer? ")
    player = Player(player_name, 100, [], all_rooms["entrance"])
    print(f"Welcome, {player.name}! Your adventure begins now.")
    print(player.current_room.description)

    while True:
        command = input("What would you like to do? (move [direction], stats, search, quit) ")
        if command.startswith("move"):
            direction = command.split()[1]
            player.move(direction)
        elif command == "stats":
            player.disp_stats()
        elif command == "search":
            player.search()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command. Please try again.")






main()