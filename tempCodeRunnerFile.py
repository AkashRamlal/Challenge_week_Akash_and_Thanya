
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