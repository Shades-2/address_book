import unittest
import address_book
from pathlib import Path


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.john = address_book.Contact("John", "email.address", "123")
        self.ab = address_book.AddressBook('contact.json')
        self.ab.add_contact('John', self.john)

    def tearDown(self):
        Path(self.ab.contactsfile).unlink()

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

    def test_search_contact(self):
        self.assertEqual(self.ab._contacts.get('John'), {
                         'name': 'John', 'email_address': 'email.address', 'phone_number': '123'})

    def test_list_contacts(self):
        self.ab.list_contacts() == ('John')


if __name__ == '__main__':
    unittest.main()
