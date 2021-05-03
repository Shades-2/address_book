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
    """Write a name for your file as the argument for the AddressBook you are instantiating. 
       This will be the file where the contacts are saved. .json will be added to the filename automatically."""

    def __init__(self, contacts_file):

        # This is where the data will be saved
        self.contacts_file = contacts_file
        self._contacts = {}

        # if the file already exists, load the data in into the _contacts dict by iterating through the file
        if Path(self.contacts_file).exists == True:
            with open(self.contacts_file) as f:
                data = json.load(f)

            for name, details in data.items():
                self._contacts[name] = Contact(
                    name, details['email_address'], details['phone_number'])

    def add_contact(self, contact):
        """add contact to address book, contact is the key you will use to find the contact and
         the value is the contact object"""
        self._contacts[contact.name] = {
            'email_address': contact.email_address, 'phone_number': contact.phone_number}

    def remove_contact(self, contact):
        """Removes contact"""
        if contact in self._contacts:
            del self._contacts[contact]
            
        else:
            raise Exception("Contact doesn't exist")

    def search_contact(self, contact):
        """ Searches the dictionary for the key passed in as an arg and returns the Contact object's detail's. """
        if contact in self._contacts:
            return None

        else:
            raise Exception("Contact doesn't exist")

    def list_contacts(self):
        """ Lists all contacts using a for in loop. """
        for ls in self._contacts.keys():
            return ls

    def save(self):
        """ Saves _contacts file to disk. """
        with open(self.contacts_file, 'w') as f:
            # Dump to the file
            json.dump(self._contacts, f, indent=2)

