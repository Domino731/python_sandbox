# APP: 06
# DATE: 22.02.2023
# Description: create an app/game to manage your contacts (number,name), user can add/delete contact

contacts = []
id = 0


def display_all_contacts():
    for contact in contacts:
        print('Contact id', contact.get('id'))
        print('Contact name', contact.get('name'))
        print('Contact number', contact.get('number'))
        print('Contact address', contact.get('address'))


def display_contacts_amount():
    print('Your book has ' + str(len(contacts)) + ' contacts')


def add_new_contact():
    contact_id = id + 1
    contact_name = input('Please enter contact name')
    contact_number = input('Please enter contact number')
    contact_address = input('Please enter contact address')
    contacts.append({"id": contact_id, "name": contact_name, "number": contact_number, "address": contact_address})


def remove_contact():
    contact_id = input('Enter id of contact that you want to delete')
    context_index = 0
    for i in enumerate(contacts):
        index = i[0]
        contact = i[1]
        contact = contacts[index]
        if contact_id == contact.get('id'):
            context_index = index
            break
    contacts.pop(context_index)


while True:
    print('1. Display all contacts')
    print('2. Display amount of contacts')
    print('3. Add new contact')
    print('4. Remove contact')

    option = int(input('Choose the option:'))

    if option == 1:
        display_all_contacts()
    elif option == 2:
        display_contacts_amount()
    elif option == 3:
        add_new_contact()
    elif option == 4:
        remove_contact()
    else:
        print('Choose valid option')
