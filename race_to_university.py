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
    while True:
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


def situation2_game_loop(items, Failure):
    situation2 = True
    ov_chipkaart_used = False
    cash_used = False
    situation4 = False 
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
        clear_screen()
        if choice == 'help':
            print("-----------------------------------------------")
            print("You helped the old man pick up his belongings. He thanks you profusely and gives you a free metro ticket.")
            print("+ 1 metro ticket")
            print("-----------------------------------------------")
            items.append("metro ticket")
        elif choice == 'ignore':
            print("-----------------------------------------------")
            print("You chose to ignore the old man and continue on your way.")
        else:
            print("Invalid choice. Please choose 'help' or 'ignore'.")
            try_again = input("press enter to try again: ")
            continue
        print("You reach the metro station. You need OV or tickets to board the metro.")
        # Inner loop for item selection only
        item_selected = False
        while not item_selected:
            item_choice = choose_item(items)
            if item_choice == "metro ticket":
                print("You used the metro ticket to board the metro....")
                items.remove("metro ticket")
                situation2 = False
                item_selected = True
                situation4 = True
                return situation4   
            elif item_choice == "OV-chipkaart":
                print("You used your OV-chipkaart to board the metro....")
                ov_chipkaart_used = True
                situation2 = False
                item_selected = True
                situation4 = True  # Placeholder for next situation
                return situation4   # Return to continue to next situation
            elif item_choice == "Cash":
                print("You used cash to buy a metro ticket and board the metro....")
                items.remove("Cash")
                situation2 = False
                item_selected = True
                situation4 = True
                return situation4
            elif item_choice in items:
                print("You can't use that item.")
                another_choice = input("Do you want to try another item? (yes/no): ").lower()
                while another_choice not in ["yes", "no"]:
                    print('please enter yes or no')
                    another_choice = input("Do you want to try another item? (yes/no): ").lower()
                if another_choice == "yes":
                    continue  # Go back to item selection
                elif another_choice == "no":
                    # Player doesn't want to try another item, ask about going home
                    item_choice = None                
            if item_choice is None:
                back_home = input("Do you want to go back home to pick up another item? (yes/no): ").lower()
                if back_home == "yes":
                    clear_screen()
                    print("-----------------------------------------------")
                    print("You went back home to picked up an OV-chipkaart.")
                    if len(items) >= 2:
                        print("You can only carry 2 items. Please choose one to leave behind.")
                        leave_item = choose_item(items)
                        print(f"You left behind: {leave_item}")
                        items.remove(leave_item)                       
                        clear_screen()
                    items.append("OV-chipkaart")
                    print("-----------------------------------------------")
                    print("you came back to the metro station. Use your item to board the metro.")
                    continue  # Continue the item selection loop with new item
                elif back_home == "no":
                    print("You wasted too much time doing nothing. You are already late for school.")
                    input("Press Enter to try again...")
                    return False
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
                    continue
        

def situation4_game_loop(items, Failure):
    situation4 = True  # Add missing variable
    classmate_helped = True
    #classmate_helped = False
    quiz_questions = [
    {
        "question": "How many study hours does 1 credit (EC) equal at Rotterdam University of Applied Sciences?",
        "options": ["a.) 20 hours", "b.) 28 hours", "c.) 40 hours"],
        "answer": ["28 hours", "b"]
    },
    {
        "question": "How many credits (EC) must a student normally obtain per year in a full-time program?",
        "options": ["a.) 45", "b.) 60", "c.) 75"],
        "answer": ["60", "b"]
    },
    {
        "question": "What is the main language of instruction and exams at CMI?",
        "options": ["a.) English", "b.) Dutch", "c.) German"],
        "answer": ["Dutch", "b"]
    },
    {
        "question": "Who is the first point of contact for a student regarding study guidance in the first year?",
        "options": ["a.) Student counselor", "b.) Learning team coach", "c.) Study advisor"],
        "answer": ["Learning team coach", "b"]
    },
    {
        "question": "How many credits must a Communication student obtain to receive a positive study recommendation after the first year?",
        "options": ["a.) 48 EC", "b.) 35 EC", "c.) 60 EC"],
        "answer": ["48 EC", "a."]
    },
    {
        "question": "Where must a student be registered in order to take an exam?",
        "options": ["a.) Studielink", "b.) Hint", "c.) Osiris"],
        "answer": ["Osiris", "c"]
    },
    {
        "question": "Which of the following is an example of fraud according to the study guide?",
        "options": ["a.) Submitting your own work", "b.) Copying or pasting without proper citation", "c.) Asking for an extra resit"],
        "answer": ["Copying or pasting without proper citation", "b."]
    },
    {
        "question": "Who handles complaints and disputes about exams at CMI?",
        "options": ["a.) Executive Board", "b.) Bureau Complaints and Disputes (BKG)", "c.) Teaching team"],
        "answer": ["Bureau Complaints and Disputes (BKG)", "b."]
    },
    {
        "question": "Who owns the intellectual property of work created by a student during their studies?",
        "options": ["a.) Always the university", "b.) In principle, the student", "c.) The teacher who graded it"],
        "answer": ["In principle, the student", "b."]
    },
    {
        "question": "What is one of the obligations of every student according to the study guide?",
        "options": ["a.) Only attend exams", "b.) Actively contribute to education and a safe learning environment", "c.) Only hand in assignments"],
        "answer": ["Actively contribute to education and a safe learning environment", "b."]
    }]
    while situation4:
        input("Press Enter to continue...")
        clear_screen()
        situation4_texts = [
            "-----------------------------------------------",
            "You finally arrive at the school gates… ", 
            "But a senior student is blocking the entrance.",
            "She crosses her arms and says:",
            "“Not so fast. If you want to pass, you have to answer my question."
            "You can not pass until you get it right!”",
            "-----------------------------------------------"
        ]
        print("\n".join(situation4_texts))
        answer = False
        try_use_item = 0
        while True:
            answer_or_use_item = input("Type 'answer' to answer her question or 'item' to use an item: ").lower()
            if answer_or_use_item == 'answer':
                clear_screen()
                break
            elif answer_or_use_item == 'item':
                clear_screen()
                item_choice = choose_item(items)
                if item_choice == "cash":
                    print("You bribed the senior student with cash to let you pass.")
                    items.remove("cash")
                    situation4 = False
                    situation5 = True
                    answer = True
                    return situation5
                    print("You successfully passed the senior student and entered the university....")
                    situation5 = True
                    situation4 = False
                    break
                elif item_choice in items:
                    print(f"You used {item_choice}, but it didn't help.")
                    try_use_item += 1
                    if try_use_item >= 3:
                        print("You lost too much time trying to use useless items. You are late for school.")
                        return False
                        break
                else:
                    print("You have no items to use.")
                    continue
            else:
             print("Invalid choice. Please choose 'answer' or 'item'.")
        while answer == False:
            question_data = random.choice(quiz_questions)
            print(question_data["question"])
            if classmate_helped:
                print("Since you helped a classmate earlier, Your classmate helped you by giving you a choice for this question.")
                options = question_data["options"]
                for option in options:
                    print(option)
                user_answer = input("Type your answer (a/b/c): ").lower()
                # Check if user_answer matches any of the correct answers
                if user_answer in [ans.lower() for ans in question_data["answer"]]:
                    print("Correct! You may pass.")
                    situation4 = False
                    situation5 = True
                    print("You successfully passed the senior student and entered the university....")
                    answer = True
                    return situation5
                else:
                    print("Incorrect answer. Try again.")
                    continue
            else:
                print("You have to answer this question correctly to pass.")
                input_answer = input("Type your answer: ").lower()
                if input_answer == question_data["answer"][0].lower() or input_answer == question_data["answer"][1].lower():
                    is_correct = True
                else:
                    is_correct = False
                    print("Incorrect answer.")
                if is_correct:
                    print("Correct! You may pass.")
                    situation4 = False
                    answer = True
                    situation5 = True
                    print("You successfully passed the senior student and entered the university....")
                    return situation5
                    break       
                else:
                    print("Incorrect answer. Try again.")
                continue

def main_game_loop():
    # Initialize game variables
    Failure = 0
    items = ["toy", "Pen"]

    if not starting_or_quit():
        return
    else:
        start_time = time.time()

    name = user_name_input()
    print(f"Welcome, {name} to the Race to University!")
    input("Press Enter to continue...")  # Pause to show welcome message
    clear_screen()
    while Failure < 4:
        # Run situation 2 (metro station)
        situation2 = situation2_game_loop(items, Failure)
        
        if situation2 is True:
            # If situation 2 succeeded, move to situation 4
            situation4 = situation4_game_loop(items, Failure)
            
            if situation4 is True:
                # Both situations completed successfully - game won!
                print("Congratulations! You have successfully navigated all situations and reached the university!")
                return
            elif situation4 is False:
                # Situation 4 failed
                Failure += 1
                if Failure >= 4:
                    print("Game Over! You are 4 times late. You failed school.")
                    return
                else:
                    print(f"You were late yesterday. You have {4 - Failure} attempts left.")
                    input("Press Enter to try again...")
                    clear_screen()
                    continue  # Restart from situation 2               
        elif situation2 is False:
            # Situation 2 failed
            Failure += 1
            if Failure >= 4:
                print("Game Over! You are 4 times late. You failed school.")
                return
            else:
                print(f"You were late yesterday. You have {4 - Failure} attempts left.")
                input("Press Enter to start your day...")
                clear_screen()
    print()
                

if __name__ == "__main__":
    while True:
        main_game_loop()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
