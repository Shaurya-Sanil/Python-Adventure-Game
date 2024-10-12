# Introduction
print("Welcome to 'The Haunted Mansion Escape'!")
print("You are a detective trapped in a haunted mansion.\n")

# First choice
print("You see two doors: one red and one black.")
choice = input("Which door do you choose? (red/black): ").strip().lower()

if choice == "red":
    print("\nYou open the red door, and it slams shut behind you.")
    print("The floor collapses, and you fall into a pit filled with spikes.")
    print("**Game Over.**")
elif choice == "black":
    print("\nYou enter the black door, hearing whispers guiding you.")
    print("You feel a pull to go deeper into the mansion.")
    print("You survived this choice and move on to the next challenge!\n")

    # Second choice
    print("You reach a hallway with a staircase and a trapdoor.")
    choice = input("What do you do? (climb/trapdoor): ").strip().lower()

    if choice == "climb":
        print("\nYou climb the staircase to the attic.")
        print("You see a glowing mirror and a chest.")
        choice = input("What do you do? (mirror/chest): ").strip().lower()

        if choice == "mirror":
            print("\nThe mirror reveals a secret escape!")
            print("**Congratulations! You've escaped!**")
        else:
            print("\nOpening the chest releases a curse.")
            print("**Game Over.**")
    else:
        print("\nOpening the trapdoor leads to a pit of spikes.")
        print("**Game Over.**")
else:
    print("\nInvalid choice. Please choose 'red' or 'black'.")
