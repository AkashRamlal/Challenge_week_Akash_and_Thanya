import time
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)

active_session = True

# gates for progression
gate1 = True
gate3 = False
gate5 = False

while active_session:

    # --- Situation 1 ---
    while gate1:
        clear_terminal()
        print("======================================")
        print("          Destination: Home           ")
        print("======================================\n")

        print("======================================")
        print("=   a: Look for your key             =")
        print("=   b: Walk to the station           =")
        print("=   c: Call mom                      =")
        print("======================================\n")

        choice = input("Your choice: ").lower()

        if choice == "a":
            clear_terminal()
            print("======================================")
            print("       You manage to find your keys   ")
            print("                                      ")
            print("         You lose 3 minutes           ")
            print("======================================\n")
            input("Press Enter to continue...")
            gate1 = False   # close this stage
            gate3 = True    # open next stage
        elif choice in ["b", "c"]:
            clear_terminal()
            print("======================================")
            print("   Interesting choice, let’s see...   ")
            print("======================================\n")
            input("Press Enter to continue...")
            gate1 = False
            gate3 = True
        else:
            print("Invalid option, try again!")
            time.sleep(1)

    # --- Situation 3 ---
    while gate3:
        clear_terminal()
        print("======================================")
        print("        Situation 3 |wip|             ")
        print("======================================\n")

        print("======================================")
        print("=   a: Placeholder choice A          =")
        print("=   b: Placeholder choice B          =")
        print("=   c: Placeholder choice C          =")
        print("======================================\n")

        choice = input("Your choice: ").lower()

        if choice in ["a", "b", "c"]:
            print("You chose something! (progressing...)")
            input("Press Enter to continue...")
            gate3 = False
            gate5 = True
        else:
            print("Invalid option, try again!")
            time.sleep(1)

    # --- Situation 5 ---
    while gate5:
        clear_terminal()
        print("======================================")
        print("        Situation 5 (WIP)             ")
        print("======================================\n")

        print("======================================")
        print("=   a: Placeholder choice A          =")
        print("=   b: Placeholder choice B          =")
        print("=   c: Placeholder choice C          =")
        print("======================================\n")

        choice = input("Your choice: ").lower()

        if choice in ["a", "b", "c"]:
            print("End of demo! 🎉 Thanks for playing.")
            input("Press Enter to exit...")
            active_session = False
            gate5 = False
        else:
            print("Invalid option, try again!")
            time.sleep(1)
