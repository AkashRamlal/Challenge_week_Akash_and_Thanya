import random
import time

def user_name_input():
    name = input("Enter your character name: ")
    if 0 < len(name) <= 10:
        if name.isalpha() and name[0].isupper():
            return name
        else:
            print("Invalid name. Please enter a name starting with an uppercase letter.")
    print("Invalid name. Please enter a name with 1-10 alphabetic characters.")
    return user_name_input()


def starting_or_quit():
    choice = input("Press 'enter' to begin or 'q' to exit: ")
    if choice == 'q':
        print("Exiting the game.")
        return False
    return True


def main_game_loop():
    situation1 = True
    situation2 = False
    situation3 = False
    situation4 = False
    situation5 = False
    items = []
    if not starting_or_quit():
        return
    else:
        start_time = time.time()

    name = user_name_input()
    print(f"Welcome, {name} to the Race to University!")

    #situation2 setup
    situation_texts = [
        "You arrive near the metro station. You have to walk across a street to get there.",
        "While walking across the street, you notice an old man drop his belongings in front of you.",
        "The old man says:'Please help me pick up these things, or a car might hit them!'",
        "Would you help the old man or continue on your way?"
    ]
    print("\n".join(situation_texts))
    choice = input("Type 'help' to assist the old man or 'ignore' to walk away: ").lower()
    if choice == 'help':
        print("You helped the old man pick up his belongings. He thanks you profusely and gives you a free metro ticket.")
        items.append("metro ticket")
    elif choice == 'ignore':
        text_ignore = ["You chose to ignore the old man and continue on your way.",
                       "You arrive at the metro station but realize you need a OV-chipkaart to board the train."]
        print("\n".join(text_ignore))
        for item in items:
            print(f"You have: {item}")
            if item == "OV-chipkaart":
                print("You use the OV-chipkaart to board the train.")
                situation2 = False
                situation3 = True
            else:
                print("You don't have an OV-chipkaart. Would you like to buy one for 5 euros? (yes/no)")
                situation2 = False
                situation3 = True

    else:
        print("Invalid choice. Please choose 'help' or 'ignore'.")
        return

if __name__ == "__main__":
    main_game_loop()