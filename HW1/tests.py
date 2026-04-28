from credit_card_validator import credit_card_validator
import unittest


class CreditCardValidator(unittest.TestCase):

    def test_prefix_4(self):
        # Tests validity of Visa using a 16 digit number and valid checksum
        self.assertTrue(credit_card_validator("4111111111111111"))

    def test_prefix_34(self):
        # Tests validity of American Express using a 15 digit number
        self.assertTrue(credit_card_validator("378282246310005"))

    def test_prefix_37(self):
        # Tests validity of American Express using a 15 digit number
        self.assertTrue(credit_card_validator("371449635398431"))

    def test_prefix_51(self):
        # Tests MasterCard using a number from the 51 55 range
        self.assertTrue(credit_card_validator("5100000000000000"))

    def test_prefix_2221(self):
        # Tests MasterCard using a number from 2221 2720
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test_invalid_length_short(self):
        # Tests Visa with a length that is too short
        self.assertFalse(credit_card_validator("411111111111111"))

    def test_invalid_length_long(self):
        # Tests Visa with a length that is too long
        self.assertFalse(credit_card_validator("41111111111111111"))

    def test_prefix_55(self):
        # Tests MasterCard using the upper limit of the 51 55 range
        self.assertTrue(credit_card_validator("5555555555554444"))

    def test_invalid_prefix_56(self):
        # Tests MasterCard with a number just outside the 51 55 range
        self.assertFalse(credit_card_validator("5600000000000003"))

    def test_prefix_2720(self):
        # Tests MasterCard using the upper limit of 2221 2720
        self.assertTrue(credit_card_validator("2720000000000005"))

    def test_invalid_prefix_2220(self):
        # Tests MasterCard with a number just below 2221 2720
        self.assertFalse(credit_card_validator("2220000000000000"))

    def test_invalid_prefix_2721(self):
        # Tests MasterCard with a number just above 2221 2720
        self.assertFalse(credit_card_validator("2721000000000004"))

    def test_invalid_prefix_35(self):
        # Tests American Express with an invalid prefix and valid length
        self.assertFalse(credit_card_validator("350000000000006"))

    def test_invalid_prefix_36(self):
        # Tests American Express with an invalid prefix and valid length
        self.assertFalse(credit_card_validator("360000000000004"))


if __name__ == '__main__':
    unittest.main()
