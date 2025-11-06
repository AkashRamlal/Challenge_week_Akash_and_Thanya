import time
import os
import random

# ---------------------------------- GAME TIMER ----------------------------------
game_time = 10 * 60  # 30 minutes in seconds
start_time = None


def time_remaining():
    if start_time is None:
        remaining = game_time
    else:
        elapsed = time.time() - start_time
        remaining = max(0, game_time - elapsed)
    minutes, seconds = divmod(int(remaining), 60)
    return f"{minutes:02d}:{seconds:02d}"


def subtract_minutes(minutes_to_remove):
    """Subtract time from the game timer."""
    global game_time
    game_time -= minutes_to_remove * 60
    if game_time < 0:
        game_time = 0


# ---------------------------------- TEXT EFFECTS ----------------------------------
def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def typewriter_effect_lines(lines, line_delay=0.5, char_delay=0.05):
    for line in lines:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        print()
        time.sleep(line_delay)


def typewriter_input(prompt, delay=0.05):
    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(delay)
    return input()


# ---------------------------------- UTILITIES ----------------------------------
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)


def user_name_input():
    name = typewriter_input("Enter your character name: ")
    if 0 < len(name) <= 10:
        if name.isalpha() and name[0].isupper():
            return name
        else:
            print("Invalid name. Please start with an uppercase letter and use only letters.")
    else:
        print("Invalid name. Please enter 1–10 letters.")
    return user_name_input()


def starting_or_quit():
    choice = typewriter_input("Press Enter to begin or 'q' to exit: ")
    if choice.lower() == 'q':
        typewriter_effect("Exiting the game...")
        return False
    return True


def check_time_over():
    global active_session, absent, game_time, winning
    if game_time <= 0:
        typewriter_effect("\n⏰ Time's up! You didn’t make it to class on time.")
        typewriter_effect("[You are marked absent for today.]\n")
        absent += 1
        winning = False
        if absent >= 4:
            typewriter_effect("You've been absent too many times... GAME OVER.")
            active_session = False
        else:
            typewriter_input("Press Enter to try again...")
            active_session = False
        return True
    return False


def print_item_list(items):
    for i, item in enumerate(items):
        typewriter_effect(f"{i + 1}. {item}")


def choose_item(items):
    while True:
        if not items:
            typewriter_effect("You have no items to choose from.")
            return None
        typewriter_effect("Your items:")
        print_item_list(items)
        choice = typewriter_input("Type the number of the item you want to select: ")
        if choice.isdigit() and 1 <= int(choice) <= len(items):
            return items[int(choice) - 1]
        else:
            print("Invalid choice. Please select a valid item number.")


def get_random_classmate():
    names = [
        "Akash", "Jad", "Santosh", "Niels", "Iris", "Andy", "Yelte", "Erwin", "Arian", "Kaan",
        "Leon", "Jalvinio", "Wessel", "Jeffrey", "Thanya", "Ruben", "Tunahan", "Rafi", "Kevin",
        "Ishpal", "Wesley"
    ]
    return random.choice(names)


# ---------------------------------- TEXT DATA ----------------------------------
choose_items_text = [
    "You wake up late! You need to hurry to school!",
    "You can pick up 2 items before you leave:"
]

gate1_text = [
    "You stand in front of your house, staring at your bicycle.",
    "You need to get to the metro station — but you’ll need your key to unlock it.",
    "",
    "What will you do?",
    "",
    "a: Look around for your key.",
    "b: Walk toward the station.",
    "c: Call your mom to ask about the key."
]

gate1_text_a = [
    "You search around the yard and finally find your keys lying near the door.",
    "[You lost 3 minutes.]"
]

gate1_text_b = [
    "You decide to walk to the station instead.",
    "It’s a long walk, but at least you’re moving.",
    "[You lost 7 minutes by walking...]"
]

gate1_text_c = [
    "You call your mom.",
    "She tells you exactly where you left the key — turns out it was on the kitchen table.",
    "[You lost 5 minutes.]"
]

gate2_text = [
    "You arrive near the metro station.",
    "",
    "You notice an old man drop his belongings in front of you.",
    "The old man says: 'Please help me pick up these things before a car hits them!'",
    "Would you help the old man or continue on your way?"
]

gate2_help = [
    "You helped the old man pick up his belongings. He thanks you profusely and gives you a free metro ticket.",
    "[+1 Metro ticket, -5 minutes]"
]

random_classmate = get_random_classmate()
gate2_5_text = [
    "You arrive in the city.",
    "You walk to the bus stop.",
    f"You see {random_classmate}, your classmate, struggling with their scooter.",
    "Would you help your classmate or continue on your way?"
]

gate2_5_help_with_phone = [
    f"You used your phone to call a mechanic for {random_classmate}.",
    "The mechanic arrives quickly and fixes the scooter.",
    f"{random_classmate} offers you a ride to the university!"
]

gate2_5_help_without_phone = [
    f"You want to help {random_classmate}, but you don't have a phone to call a mechanic.",
    "You apologize and continue on your way."
]

gate2_5_ignore = [
    f"You ignored {random_classmate} and kept walking.",
    "You feel a bit guilty, but you need to focus on getting to the university."
]

gate3_text = [
    "You arrive at the bus stop.",
    "You need an OV-chipkaart or cash to board the bus.",
    "What will you do?",
    "a: Look for your OV-chipkaart.",
    "b: Walk to the university.",
    "c: Buy a ticket from the driver."
]

gate4_text = [
    "You finally reach the school gates.",
    "A senior student is blocking the entrance.",
    "She crosses her arms and says:",
    "“Not so fast! If you want to pass, you’ll need to answer my question correctly.”"
]

quiz_questions = [
    {
        "question": "I’m tall when I’m young and short when I’m old. What am I?",
        "options": ["a.) A candle", "b.) A pencil", "c.) A tree"],
        "answer": ["a", "a candle", "candle"]
    },
    {
        "question": "What can travel around the world while staying in the same spot?",
        "options": ["a.) A stamp", "b.) A satellite", "c.) The moon"],
        "answer": ["a", "a stamp", "stamp"]
    },
    {
        "question": "What has hands but can’t clap?",
        "options": ["a.) A statue", "b.) A clock", "c.) A robot"],
        "answer": ["b", "a clock", "clock"]
    },
    {
        "question": "What gets wetter the more it dries?",
        "options": ["a.) A towel", "b.) A sponge", "c.) A cloud"],
        "answer": ["a", "a towel", "towel"]
    },
    {
        "question": "What has many keys but can’t open a single lock?",
        "options": ["a.) A janitor", "b.) A piano", "c.) A keyboard"],
        "answer": ["b", "a piano", "piano"]
    },
    {
        "question": "The more you take, the more you leave behind. What am I?",
        "options": ["a.) Footsteps", "b.) Memories", "c.) Time"],
        "answer": ["a", "footsteps"]
    },
    {
        "question": "What belongs to you, but other people use it more than you do?",
        "options": ["a.) My money", "b.) My name", "c.) My phone"],
        "answer": ["b", "my name", "name"]
    },
    {
        "question": "What has a face and two hands but no arms or legs?",
        "options": ["a.) A robot", "b.) A clock", "c.) A card"],
        "answer": ["b", "a clock", "clock"]
    },
    {
        "question": "What can you catch but not throw?",
        "options": ["a.) A ball", "b.) A cold", "c.) A butterfly"],
        "answer": ["b", "a cold", "cold"]
    },
    {
        "question": "What comes down but never goes up?",
        "options": ["a.) Rain", "b.) Age", "c.) Shadows"],
        "answer": ["a", "rain"]
    }
]

gate5_text = [
    "You finally arrive inside the building.",
    "Standing in the hallway, you realize you have no idea which classroom you're supposed to go to.",
    "You notice a few people nearby chatting.",
    "Who do you ask for help?",
    "a: Ask Mihellon.",
    "b: Ask Pascalle.",
    "c: Check your phone for directions."
]

gate6_text = [
    "You finally arrive in front of the classroom.",
    "Just as you're about to enter, you hear a voice behind you.",
    "'Not so fast! You can't enter this classroom without a laptop!' says Mihellon.",
    "What will you do?",
    "a: Show him your laptop.",
    "b: Offer him some cash.",
    "c: Go back to get your laptop."
]


starting_or_quit_choice = starting_or_quit()
if not starting_or_quit_choice:
    active_session = False

name = user_name_input()
typewriter_effect(f"Welcome, {name}, to the Race to University!")
typewriter_input("Press Enter to continue...")
start_time = time.time()

absent = 0
winning = False


# ---------------------------------- MAIN GAME LOOP ----------------------------------
while absent < 4 and not winning:
    # --- reset one play session ---
    active_session = True
    # reset timer
    game_time = 10 * 60   # 10 minutes
    start_time = time.time()
    # reset inventory & run-state flags (do NOT reset 'absent' or 'name')
    items = []
    five_euro_used = False
    ov_chipkaart_used = False
    classmate_helped = False
    choose_2_item = True

    item_selected = False
    
    while choose_2_item:
        clear_terminal()
        typewriter_effect_lines(choose_items_text)
        available_items = [
            "OV-chipkaart", "Metro ticket", "Cash", "a phone",
            "Keys", "A book", "Pen", "Water bottle", "Snack", "Laptop"
        ]
        print_item_list(available_items)

        # Choose two items
        item1, item2 = None, None
        while item1 is None:
            choice1 = typewriter_input("Choose your first item (enter number): ")
            check_time_over()
            if choice1.isdigit() and 1 <= int(choice1) <= len(available_items):
                item1 = available_items[int(choice1) - 1]
                items.append(item1)
                typewriter_effect(f"You selected: {item1}")
                time.sleep(1)
            else:
                print("Invalid choice.")
        while item2 is None:
            choice2 = typewriter_input("Choose your second item (enter number): ")
            check_time_over()
            if choice2.isdigit() and 1 <= int(choice2) <= len(available_items):
                if available_items[int(choice2) - 1] != item1:
                    item2 = available_items[int(choice2) - 1]
                    items.append(item2)
                    typewriter_effect(f"You selected: {item2}")
                    time.sleep(1)
                else:
                    print("You can’t pick the same item twice.")
            else:
                print("Invalid choice.")
        clear_terminal()
        typewriter_effect(f"You have chosen: {item1} and {item2}")
        time.sleep(1)
        choose_2_item = False
        gate1 = True
#----------------------------------------------------------------------------------------------------------------------------
        while gate1:
            clear_terminal()
            typewriter_effect(f"your time:{time_remaining()}")
            typewriter_effect_lines(gate1_text)
            if "Keys" in items:
                typewriter_effect("You use the key to unlock and ride it to the station.....")
                time.sleep(1)
                gate1 = False
                gate2 = True
                break
            choice = typewriter_input("Your choice: ").lower()
            if check_time_over():
                break
            if choice == "a":
                clear_terminal()
                subtract_minutes(3)
                check_time_over()
                typewriter_effect_lines(gate1_text_a)
                typewriter_effect(f"your time:{time_remaining()}")
                typewriter_input("Press Enter to continue...")
                if check_time_over():
                    break
                gate1 = False
                gate2 = True
            elif choice == "b":
                clear_terminal()
                subtract_minutes(7)
                if check_time_over():
                    break
                typewriter_effect_lines(gate1_text_b)
                typewriter_effect(f"your time:{time_remaining()}")
                time.sleep(1)
                gate1 = False
                gate2 = True
            elif choice == 'c':
                clear_terminal()
                subtract_minutes(5)
                if check_time_over():
                    break
                typewriter_effect_lines(gate1_text_c)
                typewriter_effect(f"your time:{time_remaining()}")
                gate1 = False
                gate2 = True
            else:
                print("Invalid option, try again!")
                time.sleep(1)
#--------------------------------------------------------------------------------------------------------------------------------
        while gate2:
            if check_time_over():
                break
            clear_terminal()
            typewriter_effect_lines(gate2_text)
            typewriter_effect(f"your time:{time_remaining()}")
            choice = typewriter_input("Type 'help' to assist the old man or 'ignore' to walk away: ").lower()
            if check_time_over():
                break
            clear_terminal()
            if choice == 'help':
                typewriter_effect_lines(gate2_help)
                if check_time_over():
                    break
                typewriter_effect(f"your time:{time_remaining()}")
                items.append("Metro ticket")
            elif choice == 'ignore':
                typewriter_effect("You chose to ignore the old man and continue on your way.")
            else:
                print("Invalid choice. Please choose 'help' or 'ignore'.")
                typewriter_input("press enter to try again: ")
                if check_time_over():
                    break
                continue

            typewriter_effect("You reach the metro station. You need OV or tickets to board the metro.")
            while not item_selected:
                item_choice = choose_item(items)
                if item_choice == "Metro ticket":
                    typewriter_effect("You used the metro ticket to board the metro....")
                    time.sleep(1)
                    items.remove("Metro ticket")
                    gate2 = False
                    item_selected = True
                    gate2_5 = True
                elif item_choice == "OV-chipkaart":
                    typewriter_effect("You used your OV-chipkaart to board the metro....")
                    time.sleep(1)
                    ov_chipkaart_used = True
                    gate2 = False
                    item_selected = True
                    gate2_5 = True
                elif item_choice == "Cash":
                    typewriter_effect("You used cash to buy a metro ticket and board the metro....")
                    time.sleep(1)
                    items.remove("Cash")
                    gate2 = False
                    item_selected = True
                    gate2_5 = True
                elif item_choice in items:
                    typewriter_effect("You can't use that item.")
                    another_choice = typewriter_input("Do you want to try another item? (yes/no): ").lower()
                    if check_time_over():
                        break
                    while another_choice not in ["yes", "no"]:
                        typewriter_effect('please enter yes or no')
                        another_choice = typewriter_input("Do you want to try another item? (yes/no): ").lower()
                        if check_time_over():
                            break
                    if another_choice == "yes":
                        subtract_minutes(3)
                        if check_time_over():
                            break
                        continue
                    elif another_choice == "no":
                        item_choice = None                
                if item_choice is None:
                    back_home = typewriter_input("Do you want to go back home to pick up another item? (yes/no): ").lower()
                    if check_time_over():
                            break
                    if back_home == "yes":
                        subtract_minutes(8)
                        if check_time_over():
                            break
                        clear_terminal()
                        typewriter_effect("You went back home to picked up an OV-chipkaart.")
                        typewriter_effect('[You lost 8 minutes....]')
                        if len(items) >= 2 and "OV-chipkaart" in items:
                            typewriter_effect("You went back home to picked up an OV-chipkaart. But you found it in your pocket.")
                            typewriter_effect('[You lost 8 minutes for nothing....]')
                        if len(items) >= 2:
                            typewriter_effect("You can only carry 2 items. Please choose one to leave behind.")
                            leave_item = choose_item(items)
                            typewriter_effect(f"You left behind: {leave_item}")
                            items.remove(leave_item)
                            clear_terminal()
                        items.append("OV-chipkaart")
                        typewriter_effect("you came back to the metro station. Use your item to board the metro.")
                        continue
                    elif back_home == "no":
                        typewriter_effect("You wasted too much time doing nothing. You are already late for school.")
                        typewriter_input("Press Enter to try again...")
                        game_time = 0
                        if check_time_over():
                            break
                        failure = True
                        gate2 = False
                        item_selected = True
                        active_session = False
                    else:
                        print("Invalid choice. Please enter 'yes' or 'no'.")
                        continue
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
        while gate2_5:
            clear_terminal()
            typewriter_effect_lines(gate2_5_text)
            typewriter_effect(f"your time:{time_remaining()}")
            choice = typewriter_input("Type 'help' to assist your classmate or 'ignore' to walk away: ").lower()
            if check_time_over():
                break
            if choice == 'help':
                if "a phone" in items:
                    typewriter_effect_lines(gate2_5_help_with_phone)
                    classmate_helped = True
                    typewriter_input("Press Enter to continue...")
                    if check_time_over():
                        break
                    gate2_5 = False
                    gate4 = True
                else:
                    typewriter_effect_lines(gate2_5_help_without_phone)
                    typewriter_input("Press Enter to continue...")
                    if check_time_over():
                        break
                    gate2_5 = False
                    gate3 = True
            elif choice == 'ignore':
                typewriter_effect_lines(gate2_5_ignore)
                gate2_5 = False
                gate3 = True
            else:
                print("Invalid choice. Please choose 'help' or 'ignore'.")
                clear_terminal()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
        while gate3:
            clear_terminal()
            typewriter_effect_lines(gate3_text)
            typewriter_effect(f"your time:{time_remaining()}")
            choice = typewriter_input("Your choice: ").lower()
            if check_time_over():
                break
            if choice == "a" and 'OV-chipkaart' in items and ov_chipkaart_used == False:
                typewriter_effect("You use yours OV chipcard to board the bus...")
                time.sleep(1)
                gate3 = False
                gate4 = True
            elif choice == 'a' and 'OV-chipkaart' in items and ov_chipkaart_used:
                subtract_minutes(2)
                typewriter_effect("You don't have enough saldo in yours OV chipcard")
                typewriter_input("Press Enter to try something else...")
                if check_time_over():
                    break
            elif choice == 'a' and 'OV-chipkaart' not in items:
                subtract_minutes(2)
                typewriter_effect("You don't have OV chipcard with you.")
                typewriter_input("Press Enter to try something else...")
                if check_time_over():
                    break
            elif choice == 'b':
                subtract_minutes(5)
                typewriter_effect("You dicided to walk to university.")
                typewriter_effect("[You lost 10 minutes by walking]")
                time.sleep(1)
                gate3 = False
                gate4 = True
            elif choice == 'c' and "Cash" in items:
                typewriter_effect("You use cash to buy a bus ticket")
                time.sleep(1)
                gate3 = False
                gate4 = True
            elif choice == 'c' and "Cash" not in items:
                typewriter_effect("You don't have cash with you.")
                typewriter_input("Press Enter to try something else...")
                if check_time_over():
                    break
            else:
                print("Invalid option, try again!")
                time.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
        while gate4:
            clear_terminal()
            typewriter_effect_lines(gate4_text)
            typewriter_effect(f"your time:{time_remaining()}")
            answer = False
            try_use_item = 0
            while True:
                answer_or_use_item = typewriter_input("Type 'answer' to answer her question or 'item' to use an item: ").lower()
                if check_time_over():
                    break
                if answer_or_use_item == 'answer':
                    clear_terminal()
                    break
                elif answer_or_use_item == 'item':
                    clear_terminal()
                    item_choice = choose_item(items)
                    if item_choice == "cash":
                        typewriter_effect("You bribed the senior student with cash to let you pass.")
                        items.remove("cash")
                        gate4 = False
                        gate5 = True
                        answer = True
                        typewriter_effect("You successfully passed the senior student and entered the university....")
                        break
                    elif item_choice in items:
                        typewriter_effect(f"You used {item_choice}, but it didn't help.")
                        subtract_minutes(3)
                        try_use_item += 1
                        if try_use_item >= 3:
                            typewriter_effect("You lost too much time trying to use useless items. You are late for school.")
                            failure = True
                            active_session = False
                            break
                        else:
                            another_choice = typewriter_input("Do you want to try another item? (yes/no): ").lower()
                            if check_time_over():
                                break
                            while another_choice not in ["yes", "no"]:
                                subtract_minutes(3)
                                print('Please enter yes or no')
                                another_choice = input("Do you want to try another item? (yes/no): ").lower()
                                if check_time_over():
                                    break
                            if another_choice == "no":
                                break
                    elif item_choice is None:
                        subtract_minutes(3)
                        typewriter_effect("You have no items to use.")
                        break
                else:
                    subtract_minutes(5)
                    print("Invalid choice. Please choose 'answer' or 'item'.")
            while answer == False:
                question_data = random.choice(quiz_questions)
                subtract_minutes(3)
                typewriter_effect(question_data["question"])
                if classmate_helped:
                    typewriter_effect("Since you helped a classmate earlier, Your classmate helped you by giving you a choice for this question.")
                    for option in question_data["options"]:
                        typewriter_effect(option)
                    user_answer = typewriter_input("Type your answer (a/b/c): ").lower()
                    if check_time_over():
                        break
                    if user_answer in [ans.lower() for ans in question_data["answer"]]:
                        typewriter_effect("Correct! You may pass.")
                        gate4 = False
                        gate5 = True
                        typewriter_effect("You successfully passed the senior student and entered the university....")
                        answer = True
                    else:
                        typewriter_effect("Incorrect answer. Try again.")
                        continue
                else:
                    typewriter_effect("You have to answer this question correctly to pass.")
                    input_answer = typewriter_input("Type your answer: ").lower()
                    if check_time_over():
                        break
                    if input_answer in [ans.lower() for ans in question_data["answer"]] :
                        is_correct = True
                    else:
                        is_correct = False
                        typewriter_effect("Incorrect answer. Hint(you can try to answer a/b/c)")
                        subtract_minutes(2)
                    if is_correct:
                        typewriter_effect("Correct! You may pass.")
                        typewriter_effect("You successfully passed the senior student and entered the university....")
                        gate4 = False
                        gate5 = True
                        answer = True       
                    else:
                        print("Incorrect answer. Try again.")
                    continue
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
        while gate5:
            time.sleep(2)
            clear_terminal()
            typewriter_effect_lines(gate5_text)
            typewriter_effect(f"Your time: {time_remaining()}")
            choice = typewriter_input("Your choice: ").lower()
            if check_time_over():
                break
            if choice == "a":
                typewriter_effect("You decide to ask Michelon. He smiles, asks how you're doing, and then explains the way.")
                typewriter_effect("[You lost 3 minutes]")
                time.sleep(1)
                gate5 = False
                gate6 = True

            elif choice == "b":
                typewriter_effect("You decide to ask Pascalle. She greets you warmly and asks how your studies are going.")
                typewriter_effect("After chatting for a while, she finally tells you the way to the classroom.")
                typewriter_effect("[You lost 5 minutes]")
                time.sleep(1)
                active_session = False
                gate5 = False
                gate6 = True

            elif choice == "c" and "a phone" in items:
                typewriter_effect("You check your phone for directions and start walking toward the classroom...")
                time.sleep(1)
                gate5 = False
                gate6 = True

            elif choice == "c" and "a phone" not in items:
                typewriter_effect("You check your pockets but realize you left your phone at home.")
                typewriter_input("Press Enter to try something else...")

            else:
                print("Invalid option, try again!")
                time.sleep(1)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        while gate6:
            clear_terminal()
            typewriter_effect_lines(gate6_text)
            choice = typewriter_input("Your choice: ").lower()
            if check_time_over():
                break
            if choice == "a" and "Laptop" in items:
                typewriter_effect("You show him your laptop as proof.")
                typewriter_effect("He nods and lets you enter the classroom.")
                typewriter_effect("🎉 CONGRATULATIONS! YOU MADE IT ON TIME! 🎉")
                winning = True
                active_session = False
                break
            elif choice == "a" and "Laptop" not in items:
                typewriter_effect("You search your backpack but realize you don’t have your laptop with you.")
                typewriter_input("Press Enter to try something else...")
                if check_time_over():
                    break
            elif choice == "b":
                typewriter_effect("You try offering him some cash, but he refuses politely.")
                typewriter_input("Press Enter to try something else...")
                if check_time_over():
                    break
            elif choice == "c":
                typewriter_effect("You consider going back to get your laptop, but there's not enough time.")
                typewriter_effect("[YOU ARE RUNNING OUT OF TIME!]")
                game_time = 0
                if check_time_over():
                    break


