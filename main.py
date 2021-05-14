from Eventmethods import User
import sys

print("~*~*~*~*  WELCOME TO Ticket Booking System *~*~*~*~*")
intro = input("Are you a 1.customer or 2.admin? ")
if intro == "1":
    print("please enter one item  \n1.login\n2.signup :")
    selection_item = int(input("your selection "))
    if selection_item == 1:
        User.login()
        todo = input("\n1.show sold tickets. \n2.buy tickets.\n3. Quit. \n\nEnter your choice: ").strip()
        if todo == '1':
            Customer.sold_display()
        elif todo == '2':
            print("Do you have any discount codes?  \n1.Yes\n2.No :")
            selection_item2 = int(input("your selection "))
            if selection_item2 == 1:
                Discount.event_off()
                Customer.book_ticket()
                print ("successful reservation")
            elif selection_item2 == 2:
                Customer.book_ticket()
                print ("successful reservation")
            else:
                print ("input is invalid")
        elif todo == '3':
            sys.exit()
        else:
            print("\nInvalid input")
            sys.exit()
    elif selection_item == 2:
        User.signup ()
elif intro=="2":
    todo = input("\n1. Add new event. \n2. Remove event. \n3.show sold tickets.\n4. Quit. \n\nEnter your choice: ").strip()
    if todo == '1':
        Admin.create_event()
    elif todo == '2':
        Admin.remove_event()
    elif todo == '3':
        Customer.sold_display()
    elif todo == '4':
        sys.exit()
    else:
        print("\nInvalid input.")
else:
    print("\nInvalid input.")
    break


