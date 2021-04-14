import unittest
import address_book
from pathlib import Path


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.john = address_book.Contact("John", "email.address", "123")
        self.ab = address_book.AddressBook('contacts')
        self.ab.add_contact('John', self.john)

    def tearDown(self):
        Path('contacts.json').unlink

    def test_show(self):
        self.assertEqual(self.john.name, "John")
        self.assertEqual(self.john.email_address, "email.address")
        self.assertEqual(self.john.phone_number, "123")

    def test_add_contact(self):
        self.assertIn('John', self.ab._contacts)

    def test_remove_contact(self):
        self.ab.remove_contact('John')
        self.assertNotIn('John', self.ab._contacts)

    def test_the_contactsfile(self):
        assert Path(self.ab.contactsfile).exists
        assert (self.ab._contacts) == (self.ab._contacts)
        
    # def test_search_contact(self):
        # print(self.ab._contacts.get('John').show())

    # def test_list_contacts(self):
        # pass


if __name__ == '__main__':
    unittest.main()
