import unittest
import address_book
from pathlib import Path


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.john = address_book.Contact("John", "email.address", "123")
        self.ab = address_book.AddressBook('contact.json')
        self.ab.add_contact(self.john)

    def test_add_contact(self):
        jack = address_book.Contact('Jack', 'jack@email.com', 234)
        self.ab.add_contact(jack)
        self.assertIn('John', self.ab._contacts)
        self.assertIn('Jack', self.ab._contacts)

    def test_remove_contact(self):
        self.ab.remove_contact('John')
        self.assertNotIn('John', self.ab._contacts)

    def test_search_contact(self):
        self.assertEqual(self.ab._contacts.get('John'), {
                         'name': 'John', 'email_address': 'email.address', 'phone_number': '123'})

    def test_list_contacts(self):
        self.ab.list_contacts() == ('John')

    def test_save(self):
        self.ab.save
        assert Path(self.ab.contacts_file).exists
        


class TestContact(unittest.TestCase):
    def setUp(self):
        self.john = address_book.Contact("John", "email.address", "123")

    def test_show(self):
        self.assertEqual(self.john.name, "John")
        self.assertEqual(self.john.email_address, "email.address")
        self.assertEqual(self.john.phone_number, "123")


if __name__ == '__main__':
    unittest.main()
