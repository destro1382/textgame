#Add item systems
#Improve combat system
#Add secret room
#enemy dictionary
#Add Town
#Replace hallway titles
#Save system

#Welcome Message
print("Welcome to Drantill")
#Initial Imports
from player import Player
from rooms import all_rooms

def main():
    #Player definition
    player_name = input("What is your name, adventurer? ")
    #Initial player stats, location
    player = Player(player_name, 100, 10, [], all_rooms["entrance"])
    #Introduction
    print(f"Welcome, {player.name}! Your adventure begins now.")
    print("----------------------------------------------------------------")
    print(player.current_room.description)
    print("----------------------------------------------------------------")
    #Combat function
    def combat(enemy):
        if player.current_room.npcs == []:
            return
        print(f"You encounter a {enemy.name}!")
        fight_flee = input("Do you want to fight or flee? (fight/flee) ")
        
        if fight_flee == "fight":
            player.health -= enemy.damage
            enemy.health -= player.damage
            print(f"You attack the {enemy.name} and deal {player.damage} damage.")
            print(f"The {enemy.name} attacks you and deals {enemy.damage} damage.")
            if enemy.health <= 0:
                print(f"You have defeated the {enemy.name}!")
                player.current_room.npcs.remove(enemy)
            elif enemy.health > 0:
                combat(enemy)
        elif fight_flee == "flee":
            print("You flee back to the previous room.")
            if direction == "south":
                player.move("north") 
            elif direction == "north":
                player.move("south")
            elif direction == "east":
                player.move("west") 
            elif direction == "west":
                player.move("east")

        else:
            print("Invalid choice. The enemy takes advantage of your hesitation and attacks you!")
            player.health -= enemy.damage
            print(f"The {enemy.name} attacks you and deals {enemy.damage} damage.")

    #Main Game Loop
    while True:
        command = input("What would you like to do? (move [direction], stats, search, quit) ")
        if command.startswith("move"):
            direction = command.split()[1]
            player.move(direction)
            print("----------------------------------------------------------------")
            if player.current_room.npcs != []:
                combat(player.current_room.npcs[0])
        elif command == "stats":
            player.disp_stats()
            print("----------------------------------------------------------------")
        elif command == "search":
            player.search()
            print("----------------------------------------------------------------")
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command. Please try again.")
        #Win/Loss Conditions
        if "Sword of Drantill" in player.inventory:
            print("Congratulations! You have found the Sword of Drantill and won the game!")
            break
        if player.health <= 0:
            print("You have died. Game over.")
            break






main()