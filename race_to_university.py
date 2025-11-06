import time
import os
import random

game_time = int(30*60)
start_time = None


def time_remaining():
    if start_time is None:
        return game_time
    elapsed = time.time() - start_time
    remaining = game_time - elapsed
    if remaining < 0:
        remaining = 0
    minutes, seconds = divmod(int(remaining), 60)
    return f"{minutes:02d}:{seconds:02d}"


def subtract_minutes(minutes_to_remove):
    """Subtract time from the game timer."""
    global game_time
    game_time -= minutes_to_remove * 60
    if game_time < 0:
        game_time = 0

def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True) #flush makes sure it prints immediately. i will implement this later in scenes function
        time.sleep(delay)
    print()


def typewriter_effect_lines(text, line_delay=0.5, char_delay=0.05):
    for line in text:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        print()  # move to next line
        time.sleep(line_delay)


def typewriter_input(prompt, delay=0.05):
    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(delay)
    return input()


def clear_terminal(): #clear the terminal
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)

def user_name_input(): #input name 
    name = typewriter_input("Enter your character name: ")
    if 0 < len(name) <= 10:
        if name.isalpha() and name[0].isupper():
            return name
        else:
            print("Invalid name. Please enter a name starting with an uppercase letter.")
    else:
        print("Invalid name. Please enter a name with 1-10 alphabetic characters.")
    return user_name_input()

def starting_or_quit():                     #start or quit
    choice = typewriter_input("Press 'enter' to begin or 'q' to exit: ")
    if choice == 'q':
        typewriter_effect("Exiting the game.")
        return False
    return True

def print_item_list(items):
    for i, item in enumerate(items):
        typewriter_effect(f"{i + 1}. {item}")

def choose_item(items):             #choose the item
    while True:
        if not items:
            typewriter_effect("You have no items to choose from.")
            return None
        typewriter_effect("Your items:")
        print_item_list(items)
        choice = typewriter_input("Type number of item you want to select: ")
        if choice.isdigit() and 1 <= int(choice) <= len(items):
            return items[int(choice) - 1]
        else:
            print("Invalid choice. Please select a valid item number.")

def classmate_name():
    names = ['Akash', "Jad", "Santosh", "Niels", "Iris", "Andy", "Yelte", 
    "Erwin", "Arian", "Kaan","Leon", "Jalvinio", "Wessel", "Jeffrey", "Thanya", "Ruben",
    "Tunahan", "Rafi", "Kevin", "Ishpal", "Wesley",'Akash', "Jad", "Santosh", "Niels", "Iris", "Andy", "Yelte", 
    "Erwin", "Arian", "Kaan","Leon", "Jalvinio", "Wessel", "Jeffrey", "Thanya", "Ruben",
    "Tunahan", "Rafi", "Kevin", "Ishpal", "Wesley"]
    return random.choice(names)


#-------------------------------------------------ALL TEXT-----------------------------------------------------------------
choose_items_text = [
    " You wake up late! You need to hurry to school!",
    "You can pick up 2 items before you leave:",
]


gate1_text = [
    "You stand in front of your house, staring at your bicycle.",
    "The lock glints faintly in the light — you’ll need your key to unlock it.",
    "",
    "What will you do?",
    "",
    "a: Look around for your key",
    "b: Walk toward the station",
    "c: Call your mom to ask about the key"
]
gate1_text_a = [
    'You manage to find your keys',
    '[You lose 3 minutes]'
]
gate1_text_b = [
    'You decide to walk to the station',
    '[You lost 7 minutes by walking.....]'
]
gate1_text_c = [
    'You called your mom',
    'She tels you where is the key',
    '[You lost 5 minutes]'
]


gate2_text = [
    "You arrive near the metro station",
    '',
    "You notice an old man drop his belongings in front of you.",
    "The old man says:'Please help me pick up these things, or a car might hit them!'",
    "Would you help the old man or continue on your way?"
]

gate2_help = [
            "You helped the old man pick up his belongings. He thanks you profusely and gives you a free metro ticket.",
            "[+ 1 Metro ticket and you lost 5 mintutes ]",
]

classmate_name = classmate_name()
gate2_5_text = [
        "You arrive in the city",
        "You walk to the bus stop.",
        f"You saw {classmate_name}. It's your classmate who's struggling with their scooter.",
        "Would you help your classmate or continue on your way?",
]
gate2_5_help_with_phone = [
                f"You used a phone to call a mechanic for {classmate_name}.",
                "The mechanic arrives quickly and helps fix the scooter.",
                f"{classmate_name} offers you a ride to the university."
]
gate2_5_help_without_phone = [
                f"You want to help {classmate_name}, but you don't have a phone to call a mechanic.",
                "You apologize and have to continue on your way.",
]
gate2_5_ignore = [
            f"You ignored {classmate_name} and continued on your way.",
            "You feel a bit guilty, but you need to focus on getting to the university."
]

gate3_text = [
        "You arrived at bus stop",
        'You need OV chipcard or cash to aboard the bus',
        'What would you do?',
        "a: Look for your OV chipcard",
        "b: Walk to university",
        "c: you buy a ticket at the bus",
]

gate4_text = [
        "You finally arrive at the school gates.",
        "A senior student is blocking the entrance.",
        "She crosses her arms and says:",
        "“Not so fast. If you want to pass, you have to answer my question.",
        "You can not pass until you get it right!”",
]
quiz_questions = [
    {
        "question": "I’m tall when I’m young and short when I’m old. What am I?",
        "options": ["a.) A candle", "b.) A pencil", "c.) A tree"],
        "answer": "a"
    },
    {
        "question": "What can travel around the world while staying in the same spot?",
        "options": ["a.) A stamp", "b.) A satellite", "c.) The moon"],
        "answer": "a"
    },
    {
        "question": "What has hands but can’t clap?",
        "options": ["a.) A statue", "b.) A clock", "c.) A robot"],
        "answer": "b"
    },
    {
        "question": "What gets wetter the more it dries?",
        "options": ["a.) A towel", "b.) A sponge", "c.) A cloud"],
        "answer": "a"
    },
    {
        "question": "What has many keys but can’t open a single lock?",
        "options": ["a.) A janitor", "b.) A piano", "c.) A keyboard"],
        "answer": "b"
    },
    {
        "question": "The more you take, the more you leave behind. What am I?",
        "options": ["a.) Footsteps", "b.) Memories", "c.) Time"],
        "answer": "a"
    },
    {
        "question": "What belongs to you, but other people use it more than you do?",
        "options": ["a.) Your money", "b.) Your name", "c.) Your phone"],
        "answer": "b"
    },
    {
        "question": "What has a face and two hands but no arms or legs?",
        "options": ["a.) A robot", "b.) A clock", "c.) A card"],
        "answer": "b"
    },
    {
        "question": "What can you catch but not throw?",
        "options": ["a.) A ball", "b.) A cold", "c.) A butterfly"],
        "answer": "b"
    },
    {
        "question": "What comes down but never goes up?",
        "options": ["a.) Rain", "b.) Age", "c.) Shadows"],
        "answer": "a"
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

active_session = True
items = []

gate1 = False
gate2 = False
gate2_5 = False
gate3 = False
gate4 = False
gate5 = False
gate6 = False

winning = False

starting_or_quit_choice = starting_or_quit()
if not starting_or_quit_choice:
    active_session = False

name = user_name_input()
typewriter_effect(f"Welcome, {name} to the Race to University!")
typewriter_input("Press Enter to continue...")
start_time = time.time()

five_euro_used = False
ov_chipkaart_used = False
classmate_helped = False
failure = False
choose_2_item = True
#-------------------------------------------------------------------------------------------------------------------
while choose_2_item:
    clear_terminal()
    typewriter_effect_lines(choose_items_text)
    available_items = ["OV-chipkaart", "Cash", "Metro ticket", "5 euro", "a phone", "Keys", "A book", "Pen", "Water bottle", "Snack", "Laptop"]
    print_item_list(available_items)
    
    # Choose first item
    item1 = None
    while item1 is None:
        choice1 = typewriter_input("Choose your first item (enter number): ")
        if choice1.isdigit() and 1 <= int(choice1) <= len(available_items):
            item1 = available_items[int(choice1) - 1]
            items.append(item1)
            typewriter_effect(f"You selected: {item1}")
            time.sleep(1)
        else:
            print("Invalid selection. Please enter a valid number.")
            time.sleep(1) 
    # Choose second item
    item2 = None
    while item2 is None:
        choice2 = typewriter_input("Choose your second item (enter number): ")
        if choice2.isdigit() and 1 <= int(choice2) <= len(available_items):
            if available_items[int(choice2) - 1] != item1:
                item2 = available_items[int(choice2) - 1]
                items.append(item2)
                typewriter_effect(f"You selected: {item2}")
                time.sleep(1)
            else:
                print("You cannot choose the same item twice. Please pick a different item.")
                time.sleep(1)
        else:
            print("Invalid selection. Please enter a valid number.")
            time.sleep(1)
    
    clear_terminal()
    typewriter_effect(f"You have chosen: {item1} and {item2}")
    time.sleep(1)
    choose_2_item = False
    gate1 = True


#-------------------------------------------------------------------------------------------------------------------
while active_session:
    while gate1:
        clear_terminal()
        typewriter_effect(f"your time:{time_remaining()}")
        typewriter_effect_lines(gate1_text)
        choice = typewriter_input("Your choice: ").lower()
        if choice == "a":
            clear_terminal()
            subtract_minutes(3)
            typewriter_effect_lines(gate1_text_a)
            typewriter_effect(f"your time:{time_remaining()}")
            typewriter_input("Press Enter to continue...")
            gate1 = False
            gate2 = True
            gate3 = True
        elif choice == "b":
            clear_terminal()
            subtract_minutes(7)
            typewriter_effect_lines(gate1_text_b)
            typewriter_effect(f"your time:{time_remaining()}")
            gate1 = False
            gate2 = True
        elif choice == 'c':
            clear_terminal()
            subtract_minutes(5)
            typewriter_effect_lines(gate1_text_c)
            typewriter_effect(f"your time:{time_remaining()}")
            gate1 = False
            gate2 = True
        else:
            print("Invalid option, try again!")
            time.sleep(1)
#-----------------------------------------------------------------------------------------------------------------------
    while gate2:
        clear_terminal()
        typewriter_effect_lines(gate2_text)
        typewriter_effect(f"your time:{time_remaining()}")
        choice = typewriter_input("Type 'help' to assist the old man or 'ignore' to walk away: ").lower()
        clear_terminal()
        if choice == 'help':
            typewriter_effect_lines(gate2_help)
            typewriter_effect(f"your time:{time_remaining()}")
            items.append("Metro ticket")
        elif choice == 'ignore':
            typewriter_effect("You chose to ignore the old man and continue on your way.")
        else:
            print("Invalid choice. Please choose 'help' or 'ignore'.")
            typewriter_input("press enter to try again: ")
            continue

        typewriter_effect("You reach the metro station. You need OV or tickets to board the metro.")
        item_selected = False
        while not item_selected:
            item_choice = choose_item(items)
            if item_choice == "Metro ticket":
                typewriter_effect("You used the metro ticket to board the metro....")
                items.remove("Metro ticket")
                gate2 = False
                item_selected = True
                gate2_5 = True
            elif item_choice == "OV-chipkaart":
                typewriter_effect("You used your OV-chipkaart to board the metro....")
                ov_chipkaart_used = True
                gate2 = False
                item_selected = True
                gate2_5 = True
            elif item_choice == "Cash":
                typewriter_effect("You used cash to buy a metro ticket and board the metro....")
                items.remove("Cash")
                gate2 = False
                item_selected = True
                gate2_5 = True
            elif item_choice in items:
                typewriter_effect("You can't use that item.")
                another_choice = typewriter_input("Do you want to try another item? (yes/no): ").lower()
                while another_choice not in ["yes", "no"]:
                    typewriter_effect('please enter yes or no')
                    another_choice = typewriter_input("Do you want to try another item? (yes/no): ").lower()
                if another_choice == "yes":
                    subtract_minutes(3)
                    continue
                elif another_choice == "no":
                    item_choice = None                
            if item_choice is None:
                back_home = typewriter_input("Do you want to go back home to pick up another item? (yes/no): ").lower()
                if back_home == "yes":
                    subtract_minutes(8)
                    clear_terminal()
                    typewriter_effect("You went back home to picked up an OV-chipkaart.")
                    typewriter_effect('[You lost 8 minutes]')
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
                    failure = True
                    gate2 = False
                    item_selected = True
                    active_session = False
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
                    continue
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    while gate2_5:
        clear_terminal()
        typewriter_effect_lines(gate2_5_text)
        typewriter_effect(f"your time:{time_remaining()}")
        choice = typewriter_input("Type 'help' to assist your classmate or 'ignore' to walk away: ").lower()
        if choice == 'help':
            if "a phone" in items:
                typewriter_effect_lines(gate2_5_help_with_phone)
                classmate_helped = True
                typewriter_input("Press Enter to continue...")
                gate2_5 = False
                gate4 = True
            else:
                typewriter_effect_lines(gate2_5_help_without_phone)
                typewriter_input("Press Enter to continue...")
                gate2_5 = False
                gate3 = True
        elif choice == 'ignore':
            typewriter_effect_lines(gate2_5_ignore)
            gate2_5 = False
            gate3 = True
        else:
            print("Invalid choice. Please choose 'help' or 'ignore'.")
            clear_terminal()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    while gate3:
        clear_terminal()
        typewriter_effect_lines(gate3_text)
        typewriter_effect(f"your time:{time_remaining()}")
        choice = input("Your choice: ").lower()
        if choice == "a" and 'OV-chipkaart' in items and ov_chipkaart_used == False:
            typewriter_effect("You use yours OV chipcard to board the bus...")
            time.sleep(1)
            gate3 = False
            gate4 = True
        elif choice == 'a' and 'OV-chipkaart' in items and ov_chipkaart_used:
            subtract_minutes(2)
            typewriter_effect("You don't have enough saldo in yours OV chipcard")
            typewriter_input("Press Enter to try something else...")
        elif choice == 'a' and 'OV-chipkaart' not in items:
            subtract_minutes(2)
            typewriter_effect("You don't have OV chipcard with you.")
            typewriter_input("Press Enter to try something else...")
        elif choice == 'b':
            subtract_minutes(5)
            typewriter_effect("You dicided to walk to university.")
            typewriter_effect("[You lost 10 minutes by walking]")
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
        else:
            print("Invalid option, try again!")
            time.sleep(1)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    while gate4:
        clear_terminal()
        typewriter_effect_lines(gate4_text)
        typewriter_effect(f"     your time:{time_remaining()}           ")
        answer = False
        try_use_item = 0
        while True:
            answer_or_use_item = typewriter_input("Type 'answer' to answer her question or 'item' to use an item: ").lower()
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
                        while another_choice not in ["yes", "no"]:
                            subtract_minutes(3)
                            print('Please enter yes or no')
                            another_choice = input("Do you want to try another item? (yes/no): ").lower()
                        if another_choice == "no":
                            break  # Go back to answer the question
                        # If yes, continue the loop to try another item
                elif item_choice is None:
                    subtract_minutes(3)
                    typewriter_effect("You have no items to use.")
                    break  # Go back to answer the question
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
                if input_answer == question_data["answer"][0].lower() or input_answer == question_data["answer"][1].lower():
                    is_correct = True
                else:
                    is_correct = False
                    typewriter_effect("Incorrect answer.")
                    subtract_minutes(2)
                if is_correct:
                    typewriter_effect("Correct! You may pass.")
                    gate4 = False
                    gate5 = True
                    typewriter_effect("You successfully passed the senior student and entered the university....")
                    break       
                else:
                    print("Incorrect answer. Try again.")
                continue
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
while gate5:
    time.sleep(2)
    clear_terminal()
    typewriter_effect_lines(gate5_text)
    typewriter_effect(f"Your time: {time_remaining()}")
    choice = typewriter_effect_lines("Your choice: ").lower()

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

    elif choice == "c" and "Phone" in items:
        typewriter_effect("You check your phone for directions and start walking toward the classroom...")
        time.sleep(1)
        gate5 = False
        gate6 = True

    elif choice == "c" and "Phone" not in items:
        typewriter_effect("You check your pockets but realize you left your phone at home.")
        typewriter_input("Press Enter to try something else...")

    else:
        print("Invalid option, try again!")
        time.sleep(1)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
while gate6:
    clear_terminal()
    typewriter_effect_lines(gate6_text)
    choice = typewriter_input("Your choice: ").lower()

    if choice == "a" and "Laptop" in items:
        typewriter_effect("You show him your laptop as proof.")
        typewriter_effect("He nods and lets you enter the classroom.")
        typewriter_effect("🎉 CONGRATULATIONS! YOU MADE IT ON TIME! 🎉")
        winning = True
        gate6 = False
        quit()

    elif choice == "a" and "Laptop" not in items:
        typewriter_effect("You search your backpack but realize you don’t have your laptop with you.")
        typewriter_input("Press Enter to try something else...")

    elif choice == "b":
        typewriter_effect("You try offering him some cash, but he refuses politely.")
        typewriter_input("Press Enter to try something else...")

    elif choice == "c":
        typewriter_effect("You consider going back to get your laptop, but there's not enough time.")
        typewriter_effect("[YOU ARE RUNNING OUT OF TIME!]")
        failure += 1


        

