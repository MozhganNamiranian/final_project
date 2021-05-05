import pandas as pd
from datetime import datetime as dt
from os import path
import hashlib
import csv
import sys
class User:

    def __init__(self, username, password):
        self.username=username
        self.password=password
    @staticmethod
    def signup():
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account["username"])

        username = input("enter your username:")
        if username in lst_username:
            print("valid username")
        password = input("enter your password:")
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
        obj_user = User(username, hash_password)

        row_account = [[obj_user.username, obj_user.password]]
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)
        return f'welcome {username}'
    @staticmethod
    def login():
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)

        lst_username = list(df_account["username"])
        count=0
        while True:
            username = input("enter your username:")
            if username in lst_username:
                print("valid username")
            password = input("enter your password:")
            hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()

            with open(file_path, 'r') as csv_account:
                csv_reader = csv.DictReader(csv_account)
                for row in csv_reader:
                    if row['username'] == self.username and row['password'] == hash_password:
                        print("successful login")
                    else:
                        print("wrong password")
                        count+=1
                        if count>3:
                            print('invalid attempt')


        obj_user = User(username, hash_password)


class Admin(User):
    def __init__(self, name):
        super().__init__(username,password)
        self.name=name

    def create_event(self):
        """method for creating events by admin"""

        file_path = "events.csv"
        eventnames = pd.read_csv(file_path)
        lst_event = list(eventnames ["eventname"])

        eventname = input("enter name of event:")
        capacity = input("enter capacity:")
        date = input ("enter date in format dd/mm/yy :")
        day,month,year = date.split('/')

        check = True
        try :
            datetime.datetime(int(year),int(month),int(day))
        except ValueError :
            check = False

        if(check) :
            print ("date is valid")
        else :
            print ("date is not valid")

        timeformat = "%H:%M:%S"
        time = input ("enter time in format %H:%M:%S:")
        try:
            validtime = datetime.datetime.strptime(time, timeformat)
        except ValueError:
            check = False
        if(check) :
            print ("time is valid")
        else :
            print ("time is not valid")

        if eventname not in lst_event:
            print("valid eventname")
        else:
            print("event exists")
        newevent = Event()

        row_event = [[newevent.eventname, newevent.capacity, newevent.date, newevent.time]]
        with open(file_path, 'a', newline='') as csv_event:
            csv_writer = csv.writer(csv_event)
            csv_writer.writerows(row_event)


    def remove_event(self):
        """method for removing events by admin"""
        file_path = "events.csv"
        eventnames = pd.read_csv(file_path)
        row_count = sum(1 for row in eventnames)
        with open(file_path, 'r') as csv_event:
                csv_reader = csv.DictReader(csv_event)
        if len(self.row_count) > 0:
            remove = input("Enter event name to remove (C to cancel): ").strip()
            if remove == 'c' or remove == 'C':
                print("Remove Cancelled.")
                return None
            try:
                for row in csv_reader:
                    if remove !=  row ['eventname']:
                        writer.writerow(row)
                        print("didn't exist")
                    else:
                        print("deleted successfully.")
            except:
                print("Invalid input.")
        else:
            print("No events.")

class Customer(User):
    def __init__(self, name, user_id, user_event):
        super().__init__(username,password)
        self.name=name
        self.user_id=user_id
        self.user_event=user_event

    def book_ticket(self):
        """method for booking ticket by customer"""
        file_path = "events.csv"
        eventnames = pd.read_csv(file_path)
        row_count = sum(1 for row in eventnames)
        with open(file_path, 'r') as csv_event:
                csv_reader = csv.DictReader(csv_event)
        if len(self.row_count) > 0:
                lis = [line.split() for line in csv_event]        # create a list of lists
                for i, x in enumerate(lis):                       #print the list items
                    print ("line{0} = {1}".format(i, x))
                    event.bookticket_info(i)
        preferred_event = input("Select event number (C to cancel): ").strip()
        if preferred_event == 'c' or preferred_event == 'C':
            print("Booking Cancelled.")
            return None
        try:
                preferred_event = int(preferred_event) - 1
                if preferred_event not in lis:
                    raise ValueError('Invalid input')
        except:
            print("Invalid input")
            return None
            self.events[preferred_event].book_ticket()
        else:
            print("No events available.")


class Event:
    def __init__(self, date, time, location, totalcapacity, remaincapacity, ticketprice):
        self.date=date
        self.time=time
        self.location=location
        self.remaincapacity=remaincapacity
        self.ticketprice=ticketprice
        self.totalcapacity = input("Enter the capacity: ").strip()
        while type(self.capacity) != int:
            try:
                self.totlacapacity = int(self.totlacapacity)
            except:
                self.totlacapacity = input("Invalid input. please enter an integer: ")
        self.remaincapacity = self.capacity

    def bookticket_info(self,i):
        print('{:<20}'.format(str(i + 1)) + '{:<40}'.format(self.name) + '{:<20}'.format(str(self.remaincapacity)))

    def seat_ticket(self):
        seatchoice = input("Enter number of seats to book: ").strip()
        try:
            seatchoice = int(seatchoice)
        except:
            print("Invalid input")
            return None

        if self.remaincapacity >= seatchoice:
            self.remaincapacity -= seatchoice
            print(str(seatchoice) + " ticket booked successfully for the event " + self.name)
        else:
            print(str(seatchoice) + " ticket not available.")

class Discount(Event):

    def event_off(self):
        age = int(input('Enter age: '))
        discount = get_discount(age)
        print_discount(discount)

        self.ticketprice = 20
        disc_off = calculate_discount(self.ticketprice, discount)

        print(f'  Your price: {disc_off} (initial price: {self.ticketprice})')


    def get_discount(age):
        if age <= 20:
            discount = 0.2
        elif age >= 60:
            discount = 0.3
        else:
            discount = 0.0

        return discount

    def print_discount(discount):
        if discount == 0.0:
            print('  No discount.')
        else:
            print('  Available discount: {}%'.format(int(discount * 100)))

    def calculate_discount(ticketprice, discount):
        return round(self.ticketprice - self.ticketprice * discount, 2)




