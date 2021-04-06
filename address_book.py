import pickle
from pathlib import Path

contactsfile = Path('.')


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
    def __init__(self):
        # should be private self._contracts encapsulation of data.
        self.contacts = {}

    def add_contact(self, contact, object):
        """add contact to address book, contact is the key you will use to find the contact and
         the value is the contact object"""
        self.contacts[contact] = object

        # Name of the file that will store the address book object
        # Write to the file
        f = open(contactsfile, 'wb')
        # Dump to the file

        # Can we save just the data. Preferable in json format (use json lib ie import json)??
        pickle.dump(self.contacts, f)
        f.close()
        print("Added Contact", contact)

    def remove_contact(self, contact):
        """Removes contact"""
        if contact in self.contacts:
            del self.contacts[contact]

            # Name of the file that will store the address book object
            # Write to the file
            f = open(contactsfile, 'wb')
            # Dump to the file
            pickle.dump(self.contacts, f)
            f.close()
            print("Removed Contact", contact)

        else:
            print("Could not delete contact, contact does not exist.")

    def search_contact(self, contact):
        """searches the dictionary for the key passed in as an arg and returns the Contact object's detail's"""
        if contact in self.contacts:
            print(self.contacts.get(contact).show())

        else:
            print("Contact not found.")

    def list_contacts(self):
        """Lists all contacts using a for in loop"""
        for k in self.contacts.keys():
            print(k)


# if __name__ == '__main__':
# Or put in function .. def test_adress_book():
jamie = Contact("Jamie", "jamie@hotmail.com", "01273")
ab = AddressBook()
ab.add_contact("Jamie", jamie)
