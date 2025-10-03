import time
import os
import random

def clear_terminal(): #clear the terminal
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)

def user_name_input(): #input name 
    name = input("Enter your character name: ")
    if 0 < len(name) <= 10:
        if name.isalpha() and name[0].isupper():
            return name
        else:
            print("Invalid name. Please enter a name starting with an uppercase letter.")
    else:
        print("Invalid name. Please enter a name with 1-10 alphabetic characters.")
    return user_name_input()

def starting_or_quit():                     #start or quit
    choice = input("Press 'enter' to begin or 'q' to exit: ")
    if choice == 'q':
        print("Exiting the game.")
        return False
    return True

def print_item_list(items):
    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")

def choose_item(items):             #choose the item
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

active_session = True
items = ["toy", "Pen"]

gate1 = True
gate2 = False
gate3 = False
gate4 = False
gate5 = False

starting_or_quit_choice = starting_or_quit()
if not starting_or_quit_choice:
    active_session = False

name = user_name_input()
print(f"Welcome, {name} to the Race to University!")
input("Press Enter to continue...")
clear_terminal()

five_euro_used = False
ov_chipkaart_used = False
classmate_helped = False
failure = False
#-------------------------------------------------------------------------------------------------------------------
while active_session:
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
            print("         You lose 3 minutes           ")
            print("======================================\n")
            input("Press Enter to continue...")
            gate1 = False
            gate2 = True
            gate3 = True
        elif choice in ["b", "c"]:
            clear_terminal()
            print("======================================")
            print("   Interesting choice, let’s see...   ")
            print("======================================\n")
            input("Press Enter to continue...")
            gate1 = False
            gate2 = True
        else:
            print("Invalid option, try again!")
            time.sleep(1)
#-----------------------------------------------------------------------------------------------------------------------
    while gate2:
        clear_terminal()
        print("======================================")
        print("   You arrive near the metro station  ")
        print("======================================\n")
        print("===================================================================================")
        print("You notice an old man drop his belongings in front of you.")
        print("The old man says:'Please help me pick up these things, or a car might hit them!'")
        print("Would you help the old man or continue on your way?")
        print("==================================================================================\n")
        choice = input("Type 'help' to assist the old man or 'ignore' to walk away: ").lower()
        clear_terminal()
        if choice == 'help':
            print("================================================================================================================")
            print("You helped the old man pick up his belongings. He thanks you profusely and gives you a free metro ticket.")
            print("+ 1 metro ticket")
            print("================================================================================================================")
            items.append("metro ticket")
        elif choice == 'ignore':
            print("===========================================================")
            print("You chose to ignore the old man and continue on your way.")
        else:
            print("Invalid choice. Please choose 'help' or 'ignore'.")
            input("press enter to try again: ")
            continue

        print("You reach the metro station. You need OV or tickets to board the metro.")
        item_selected = False
        while not item_selected:
            item_choice = choose_item(items)
            if item_choice == "metro ticket":
                print("You used the metro ticket to board the metro....")
                items.remove("metro ticket")
                gate2 = False
                item_selected = True
                gate3 = True
            elif item_choice == "OV-chipkaart":
                print("You used your OV-chipkaart to board the metro....")
                ov_chipkaart_used = True
                gate2 = False
                item_selected = True
                gate3 = True
            elif item_choice == "Cash":
                print("You used cash to buy a metro ticket and board the metro....")
                items.remove("Cash")
                gate2 = False
                item_selected = True
                gate3 = True
            elif item_choice in items:
                print("You can't use that item.")
                another_choice = input("Do you want to try another item? (yes/no): ").lower()
                while another_choice not in ["yes", "no"]:
                    print('please enter yes or no')
                    another_choice = input("Do you want to try another item? (yes/no): ").lower()
                if another_choice == "yes":
                    continue
                elif another_choice == "no":
                    item_choice = None                
            if item_choice is None:
                back_home = input("Do you want to go back home to pick up another item? (yes/no): ").lower()
                if back_home == "yes":
                    clear_terminal()
                    print("========================================================================")
                    print("You went back home to picked up an OV-chipkaart.")
                    if len(items) >= 2:
                        print("You can only carry 2 items. Please choose one to leave behind.")
                        leave_item = choose_item(items)
                        print(f"You left behind: {leave_item}")
                        items.remove(leave_item)
                        clear_terminal()
                    items.append("OV-chipkaart")
                    print("========================================================================")
                    print("you came back to the metro station. Use your item to board the metro.")
                    continue
                elif back_home == "no":
                    print("You wasted too much time doing nothing. You are already late for school.")
                    input("Press Enter to try again...")
                    failure = True
                    gate2 = False
                    item_selected = True
                    active_session = False
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
                    continue
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    while gate3:
        clear_terminal()
        print("======================================")
        print("        Destination: Bus Stop       ")
        print("======================================\n")
        print("======================================")
        print("=   a: Look for your OV chipcard     =")
        print("=   b: You ask ur friend for help    =")
        print("=   c: you buy a ticket at the bus   =")
        print("======================================\n")
        choice = input("Your choice: ").lower()
        if choice in ["a", "b", "c"]:



            print("You chose something! (progressing...)")
            time.sleep(30)
            input("Press Enter to continue...")
            gate3 = False
            gate4 = True
        else:
            print("Invalid option, try again!")
            time.sleep(1)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    while gate4:
        quiz_questions = [
            {"question": "How many study hours does 1 credit (EC) equal at Rotterdam University of Applied Sciences?", "options": ["a.) 20 hours", "b.) 28 hours", "c.) 40 hours"], "answer": ["28 hours", "b"]},
            {"question": "How many credits (EC) must a student normally obtain per year in a full-time program?", "options": ["a.) 45", "b.) 60", "c.) 75"], "answer": ["60", "b"]},
            {"question": "What is the main language of instruction and exams at CMI?", "options": ["a.) English", "b.) Dutch", "c.) German"], "answer": ["Dutch", "b"]},
            {"question": "Who is the first point of contact for a student regarding study guidance in the first year?", "options": ["a.) Student counselor", "b.) Learning team coach", "c.) Study advisor"], "answer": ["Learning team coach", "b"]},
            {"question": "How many credits must a Communication student obtain to receive a positive study recommendation after the first year?", "options": ["a.) 48 EC", "b.) 35 EC", "c.) 60 EC"], "answer": ["48 EC", "a."]},
            {"question": "Where must a student be registered in order to take an exam?", "options": ["a.) Studielink", "b.) Hint", "c.) Osiris"], "answer": ["Osiris", "c"]},
            {"question": "Which of the following is an example of fraud according to the study guide?", "options": ["a.) Submitting your own work", "b.) Copying or pasting without proper citation", "c.) Asking for an extra resit"], "answer": ["Copying or pasting without proper citation", "b."]},
            {"question": "Who handles complaints and disputes about exams at CMI?", "options": ["a.) Executive Board", "b.) Bureau Complaints and Disputes (BKG)", "c.) Teaching team"], "answer": ["Bureau Complaints and Disputes (BKG)", "b."]},
            {"question": "Who owns the intellectual property of work created by a student during their studies?", "options": ["a.) Always the university", "b.) In principle, the student", "c.) The teacher who graded it"], "answer": ["In principle, the student", "b."]},
            {"question": "What is one of the obligations of every student according to the study guide?", "options": ["a.) Only attend exams", "b.) Actively contribute to education and a safe learning environment", "c.) Only hand in assignments"], "answer": ["Actively contribute to education and a safe learning environment", "b."]}
        ]
        clear_terminal()
        print("========================================")
        print("You finally arrive at the school gates.")
        print("========================================\n")
        print("=====================================================================") 
        print("A senior student is blocking the entrance.")
        print("She crosses her arms and says:")
        print("“Not so fast. If you want to pass, you have to answer my question.")
        print("You can not pass until you get it right!”")
        print("=====================================================================\n")
        answer = False
        try_use_item = 0
        while True:
            answer_or_use_item = input("Type 'answer' to answer her question or 'item' to use an item: ").lower()
            if answer_or_use_item == 'answer':
                clear_terminal()
                break
            elif answer_or_use_item == 'item':
                clear_terminal()
                item_choice = choose_item(items)
                if item_choice == "cash":
                    print("You bribed the senior student with cash to let you pass.")
                    items.remove("cash")
                    gate4 = False
                    gate5 = True
                    answer = True
                    print("You successfully passed the senior student and entered the university....")
                    break
                elif item_choice in items:
                    print(f"You used {item_choice}, but it didn't help.")
                    try_use_item += 1
                    if try_use_item >= 3:
                        print("You lost too much time trying to use useless items. You are late for school.")
                        failure = True
                        active_session = False
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
                for option in question_data["options"]:
                    print(option)
                user_answer = input("Type your answer (a/b/c): ").lower()
                if user_answer in [ans.lower() for ans in question_data["answer"]]:
                    print("Correct! You may pass.")
                    gate4 = False
                    gate5 = True
                    print("You successfully passed the senior student and entered the university....")
                    answer = True
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
                    gate4 = False
                    gate5 = True
                    print("You successfully passed the senior student and entered the university....")
                    break       
                else:
                    print("Incorrect answer. Try again.")
                continue
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    while gate5:
        clear_terminal()
        print("======================================")
        print("   Location: hogeschool rotterdam     ")
        print("======================================\n")
        print("======================================")
        print("=   a: You ask Michelon              =")
        print("=   b: you ask pascalle              =")
        print("=   c: you look on your phone        =")
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
