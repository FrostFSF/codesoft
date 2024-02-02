import os
from colorama import Fore, init, Style

init(autoreset=False)


class Format:
    def __init__(self) -> None:
        self.grey = Fore.LIGHTBLACK_EX
        self.blue = Fore.LIGHTBLUE_EX
        self.default = Fore.WHITE
        self.green = Fore.LIGHTGREEN_EX
        self.purple = Fore.LIGHTMAGENTA_EX

class Console:
    def clear(self) -> None:
        os.system('cls')

class ContactBook:
    def __init__(self) -> None:
        self.user_list = []
        self.total_users = 0

    def __createNewContact__(self, name, phone, address) -> object:
        user = {'id': self.total_users, 'name': name, 'phonenumber': phone, 'address': address}
        self.total_users += 1
        return user
        
    def addContact(self) -> None:
        name = input("Enter name of the user: ")
        phone = input("Enter phone of the user: ")
        address = input("Enter address of the user: ")

        self.user_list.append(self.__createNewContact__(name, phone, address))
    
    def findContact(self, filter) -> object:
        for user in self.user_list:
            if all(user.get(key) == value for key, value in filter.items()):
                return {'found': True, 'id': user.get('id'), 'user-info': user}
        return {'found': False}
    
    def updateUser(self, filter, updateInfo) -> object:
        user = self.findContact(filter)
        if(user['found']):
            user = self.user_list[user['id']]
            for key, value in updateInfo.items():
                user[key] = value
            return {'status': True}
        else:
            return {'status': False}

    def __shift_elements__(self, fromPosition, arr) -> list:
        if(fromPosition == 0):
            for from_pos in range(fromPosition, len(arr) - 1):
                arr[from_pos] = arr[from_pos + 1]
                arr[from_pos]['id'] = arr[from_pos + 1]['id'] - 1
            arr = arr[:-1]
        elif(fromPosition == len(arr) - 1):
            arr = arr[:-1]
        else:
            for from_pos in range(fromPosition, len(arr) - 1):
                arr[from_pos] = arr[from_pos + 1]
                arr[from_pos]['id'] = arr[from_pos + 1]['id'] - 1
            arr = arr[:-1]
        self.total_users -= 1
        return arr

    def deleteContact(self, filter) -> object:
        user = self.findContact(filter)
        if(user['found']):
            self.user_list = self.__shift_elements__(user['id'], self.user_list)
            return {'status': True}
        else:
            return {'status': False}

    def set_filter(self) -> object:
        print(f"{formatting_options.grey}Select Filtering Options:{formatting_options.default} \n")
        print("1) By Name")
        print("2) By Phone Number")
        print("3) By Name and Phone Number")
        print("4) Exit")
        
        filter = {}

        user_choice = int(input("Enter your choice: "))
        if(user_choice == 1):
            name = input("Enter contact name: ")
            filter = {'name': name}
        elif(user_choice == 2):
            phonenumber = input("Enter contact phonenumber: ")
            filter = {'phonenumber': phonenumber}
        elif(user_choice == 3):
            name = input("Enter contact name: ")
            phonenumber = input("Enter contact phonenumber: ")
            filter = {'name': name,'phonenumber': phonenumber}
        elif(user_choice == 4):
            return filter        
        return filter

    def set_update_filter(self) -> object:
        print("Enter new information for the contact. Leave a field empty for no change.")

        name = input("Enter contact new name: ")
        phonenumber = input("Enter contact new phonenumber: ")
        address = input("Enter contact new address: ")

        update_filter = {}

        if name.strip():
            update_filter['name'] = name
        if phonenumber.strip():
            update_filter['phonenumber'] = phonenumber
        if address.strip():
            update_filter['address'] = address

        return update_filter
    
    def print_list(self) -> None:
        if(not self.user_list):
            print(f'{formatting_options.grey}List is Empty!{formatting_options.default}')
            input("\nEnter to continue: ")
            return
        
        for user in self.user_list:
            print(f'{formatting_options.blue}Name{formatting_options.default}: {user["name"]}   {formatting_options.blue}Phone Number{formatting_options.default}: {user["phonenumber"]}   {formatting_options.blue}Address{formatting_options.default}: {user["address"]}')
        
        input("\nEnter to continue: ")


console = Console()
formatting_options = Format()
end = False
contact_book = ContactBook()
previous_output = ''

while not end:
    console.clear()
    print(f'{previous_output}\n')
    print("1) Add user to Contact Book")
    print("2) Find user from Contact Book")
    print("3) Update user from Contact Book")
    print("4) Delete user from Contact Book")
    print("5) List all users in Contact Book")
    print("6) Exit")

    userChoice = int(input("Enter your choice: "))

    if(userChoice == 1):
        contact_book.addContact()
        previous_output = f'Previous Output: {formatting_options.grey}User added!{formatting_options.default}'

    elif(userChoice == 2):
        console.clear()
        filter = contact_book.set_filter()

        if(not filter):
            previous_output = f'{formatting_options.grey}Exited Successfully!{formatting_options.default}'

        user = contact_book.findContact(filter)
        if(user['found']):
            previous_output = f'Previous Output: {formatting_options.blue}Name{formatting_options.default}: {user["user-info"]["name"]}   {formatting_options.blue}Phone Number{formatting_options.default}: {user["user-info"]["phonenumber"]}   {formatting_options.blue}Address{formatting_options.default}: {user["user-info"]["address"]}'
        else:
            previous_output = f'Previous Output: {formatting_options.grey}User Not Found!{formatting_options.default}'

    elif(userChoice == 3):
        console.clear()
        filter = contact_book.set_filter()
        console.clear()
        updating_filter = contact_book.set_update_filter()
        
        result = contact_book.updateUser(filter,updating_filter)

        if(result['status']):
            previous_output = f'Previous Output: {formatting_options.grey}User Updated Successfully!{formatting_options.default}'
        else:
            previous_output = f'Previous Output: {formatting_options.grey}User Not Found!{formatting_options.default}'
        
    elif(userChoice == 4):
        console.clear()
        filter = contact_book.set_filter()
        result = contact_book.deleteContact(filter)

        if(result['status']):
            previous_output = f'Previous Output: {formatting_options.grey}User Deleted Successfully!{formatting_options.default}'
        else:
            previous_output = f'Previous Output: {formatting_options.grey}User Not Found!{formatting_options.default}'

    elif(userChoice == 5):
        console.clear()
        contact_book.print_list()
        previous_output = f'Previous Output: {formatting_options.grey}List shown successully!{formatting_options.default}'
        pass
    elif(userChoice == 6):
        break
    else:
        previous_output = f'Previous Output: {formatting_options.grey}Invalid Output{formatting_options.default}'
