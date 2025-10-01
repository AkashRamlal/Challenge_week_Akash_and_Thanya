import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def user_name_input():
    name = input("Enter your character name: ")
    if 0 < len(name) <= 10:
        if name.isalpha() and name[0].isupper():
            return name
        else:
            print("Invalid name. Please enter a name starting with an uppercase letter.")
    else:
        print("Invalid name. Please enter a name with 1-10 alphabetic characters.")
    return user_name_input()


def starting_or_quit():
    choice = input("Press 'enter' to begin or 'q' to exit: ")
    if choice == 'q':
        print("Exiting the game.")
        return False
    return True

def print_item_list(items):
    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")


def choose_item(items):
    if not items:
        print("You have no items to choose from.")
        return None
    print("Your items:")
    print_item_list(items)
    choice = input("Type number of item you want to select: ")
    if choice.isdigit() and 1 <= int(choice) <= len(items):
        return items[int(choice) - 1]
    else:
        print("Invalid choice. Please select a valid item number.")
        return choose_item(items)


def main_game_loop():
    Failure = 0
    situation1 = False
    situation2 = False
    situation3 = False
    situation4 = False
    situation5 = False
    ov_chipkaart_used = False
    items = ["toy", "Pen"]
    if not starting_or_quit():
        return
    else:
        start_time = time.time()

    name = user_name_input()
    print(f"Welcome, {name} to the Race to University!")
    input("Press Enter to continue...")  # Pause to show welcome message

    situation1 = False
    situation2 = True
    while situation2:
        clear_screen()
        #situation2 setup
        situation_texts = [
            "-----------------------------------------------",
            "You arrive near the metro station. You have to walk across a street to get there.",
            "While walking across the street, you notice an old man drop his belongings in front of you.",
            "The old man says:'Please help me pick up these things, or a car might hit them!'",
            "Would you help the old man or continue on your way?",
            "-----------------------------------------------"
        ]
        print("\n".join(situation_texts))
        choice = input("Type 'help' to assist the old man or 'ignore' to walk away: ").lower()
        if choice == 'help':
            print("You helped the old man pick up his belongings. He thanks you profusely and gives you a free metro ticket.")
            items.append("metro ticket")
            clear_screen()
        elif choice == 'ignore':
            print("You chose to ignore the old man and continue on your way.")
            clear_screen()
        else:
            print("Invalid choice. Please choose 'help' or 'ignore'.")
            try_again = input("press enter to try again: ")
            continue
        print("You reach the metro station. You need OV or tickets t board the metro.")

        
        # Inner loop for item selection only
        item_selected = False
        while not item_selected:
            item_choice = choose_item(items)
            if item_choice == "metro ticket":
                print("You used the metro ticket to board the metro.")
                items.remove("metro ticket")
                situation2 = False
                situation3 = True
                item_selected = True
            elif item_choice == "OV-chipkaart":
                print("You used your OV-chipkaart to board the metro.")
                ov_chipkaart_used = True
                situation2 = False
                situation3 = True
                item_selected = True
            elif item_choice == "Cash":
                print("You used cash to buy a metro ticket and board the metro.")
                items.remove("Cash")
                situation2 = False
                situation3 = True
                item_selected = True
            elif item_choice in items:
                print("You can't use that item.")
                another_choice = input("Do you want to try another item? (yes/no): ").lower()
                while another_choice not in ["yes", "no"]:
                    print('please enter yes or no')
                    another_choice = input("Do you want to try another item? (yes/no): ").lower()
                if another_choice == "yes":
                    continue
                else:
                    item_choice = None
            if item_choice is None:
                back_home = input("Do you want to go back home to pick up another item? (yes/no): ").lower()
                if back_home == "yes":
                    clear_screen()
                    print("You went back home to picked up an OV-chipkaart.")
                    if len(items) >= 2:
                        print("You can only carry 2 items. Please choose one to leave behind.")
                        leave_item = choose_item(items)
                        print(f"You left behind: {leave_item}")
                        items.remove(leave_item)
                        clear_screen()
                    items.append("OV-chipkaart")
                    print("you came back to the metro station. Use your item to board the metro.")
                    continue  # Continue the item selection loop with new item
                else:
                    print("You wasted too much time doing nothing. You already late for school.")
                    Failure += 1
                    if Failure >= 3:
                        print("You have failed to reach the university on time. Game over.")
                        return
                    else:
                        print(f"Failure count: {Failure}/3. Try again!")
                        break  # Break out of the item selection loop to restart the situation 

if __name__ == "__main__":
    while True:
        main_game_loop()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break