import unittest
from behave import given, then
from validator import Validator

class StepDefinition(unittest.TestCase):
    @given("User have provided the credentials")
    def setup(self):
        print("Credential Received, Starting Validation")

    @then("Verify the password")
    def verify_password(self):
        es = Validator()
        print(es.password_is_valid("Andrei123"))

    @then("Verify the username")
    def verify_username(self):
        es = Validator()
        print(es.username_is_valid("Andrei"))

if __name__ == "__main__":
    unittest.main()
