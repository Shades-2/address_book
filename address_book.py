from pathlib import Path
import json
# change to being able to take an arguement so the file can be whatever.
contactsfile = Path('contacts.json')


class Contact:
    def __init__(self, name, email_address, phone_number):
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number

    def show(self):
        """Shows details."""
        print(
            f'Name = {self.name}, Email Address = {self.email_address}, Phone number = {self.phone_number}')

# 1 arg is name of contactsfile
# need to be able to handle contacts file doesnt exist or exists
# if exist you load the data in json into _contacts
# save the filename self.contactsfile = contacts
class AddressBook:
    def __init__(self):
        self._contacts = {}

    def add_contact(self, contact, object):
        """add contact to address book, contact is the key you will use to find the contact and
         the value is the contact object"""
        self._contacts[contact] = vars(object)

        # Name of the file that will store the address book object
        # Write to the file
        with open(contactsfile, 'w') as f:
            # Dump to the file
            json.dump(self._contacts, f)

        print("Added Contact", contact)

    def remove_contact(self, contact):
        """Removes contact"""
        if contact in self._contacts:
            del self._contacts[contact]

            # Name of the file that will store the address book object
            # Write to the file
            with open(contactsfile, 'w') as f:
                # Dump to the file
                json.dump(self._contacts, f)
            print("Removed Contact", contact)

        else:
            print("Could not delete contact, contact does not exist.")

    def search_contact(self, contact):
        """searches the dictionary for the key passed in as an arg and returns the Contact object's detail's"""
        if contact in self._contacts:
            print(self._contacts.get(contact).show())

        else:
            print("Contact not found.")

    def list_contacts(self):
        """Lists all contacts using a for in loop"""
        for ls in self._contacts.keys():
            print(ls)


# if __name__ == '__main__':
# Or put in function .. def test_adress_book():
john = Contact("John", "email.address", "123")
ab = AddressBook()
ab.add_contact('John', john)
ab.search_contact('John')