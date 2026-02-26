import unittest
from encryption import encrypt, decrypt


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = "Dublin"

    def test_message_length(self):
        with self.assertRaises(ValueError):
            encrypt("A")

    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))

    def test_differentIO(self):
        self.assertNotEqual(self.my_message, encrypt(self.my_message))

    def test_encryption(self):
        self.assertEqual("Evcmjo", encrypt(self.my_message))

    def test_decryption(self):
        self.assertEqual("Dublin", decrypt(encrypt(self.my_message)))

    def test_unsupported_character_raises_error(self):
        with self.assertRaises(ValueError):
            encrypt("DublinÑ")

    def test_alternative_shift_encrypt(self):
        self.assertEqual("Fwdnkp", encrypt("Dublin", 2))

    def test_alternative_shift_decrypt(self):
        self.assertEqual("Dublin", decrypt("Fwdnkp", 2))

if __name__ == '__main__':
    unittest.main()