class Validator:
    def password_is_valid(self, password):
        if len(password) >= 5 and len(password) <= 10:
            return True
        else:
            return False

    def username_is_valid(self, username):
        if len(username) >= 3 and len(username) <= 7:
            return True
        else:
            return False
