from pathlib import Path
import json


class Contact:
    def __init__(self, name, email_address, phone_number):
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number

    def show(self):
        """Shows details."""
        print(
            f'Name = {self.name}, Email Address = {self.email_address}, Phone number = {self.phone_number}')


class AddressBook:
    '''Write a name for your file as the argument for the AddressBook you are instantiating. 
       This will be the file where the contacts are saved. .json will be added to the filename automatically.'''
    # dont need to duplicate name

    def __init__(self, contactsfile):
        # This is where the data will be saved
        self.contactsfile = contactsfile
        self._contacts = {}
        # if the file already exists, load the data in into the _contacts dict by iterating through the file
        if Path(self.contactsfile).exists == True:
            with open(self.contactsfile) as f:
                data = json.load(f)

            for name, details in data.items():
                self._contacts[name] = Contact(
                    name, details['email_address'], details['phone_number'])

        elif Path(self.contactsfile).exists == False:
            open(self.contactsfile)

    def add_contact(self, contact, object):
        """add contact to address book, contact is the key you will use to find the contact and
         the value is the contact object"""
        self._contacts[contact] = vars(object)

        # Name of the file that will store the address book object
        # Write to the file
        with open(self.contactsfile, 'w') as f:
            # Dump to the file
            json.dump(self._contacts, f, indent=2)

        print("Added Contact", contact)

    def remove_contact(self, contact):
        """Removes contact"""
        if contact in self._contacts:
            del self._contacts[contact]

            # Name of the file that will store the address book object
            # Write to the file
            with open(self.contactsfile, 'w') as f:
                # Dump to the file
                json.dump(self._contacts, f)
            print("Removed Contact", contact)

        else:
            print("Could not delete contact, contact does not exist.")

    def search_contact(self, contact):
        """searches the dictionary for the key passed in as an arg and returns the Contact object's detail's"""
        if contact in self._contacts:
            print(self._contacts.get(contact))

        else:
            print("Contact not found.")

    def list_contacts(self):
        """Lists all contacts using a for in loop"""
        for ls in self._contacts.keys():
            print(ls)
