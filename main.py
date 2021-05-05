from Eventmethods import User

print("~*~*~*~*  WELCOME TO Ticket Booking System *~*~*~*~*")
intro = input("Are you a 1.customer or 2.admin? ")
if intro == "1":
    print("please enter one item  \n1.login\n2.signup :")
    selection_item = int(input("your selection "))
    if selection_item == 1:
        User.login()
        todo = input("\n1.show sold tickets. \n2.buy tickets.\n3. Quit. \n\nEnter your choice: ").strip()
        if todo == '1':
            sold_display()
        elif todo == '2':
            book_ticket()
        elif todo == '3':
            break
        else:
            print("\nInvalid input")
            break
    elif selection_item == 2:
        User.signup ()
elif intro=="2":
    todo = input("\n1. Add new event. \n2. Remove event. \n3.show sold tickets.\n4. Quit. \n\nEnter your choice: ").strip()
    if todo == '1':
        create_event()
    elif todo == '2':
        remove_event
    elif todo == '3':
        sold_display
    elif todo == '4':
        sys.exit()
    else:
        print("\nInvalid input.")
else:
    print("\nInvalid input.")
    break


