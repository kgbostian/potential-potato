class User:
    def __init__(self, username, passwd="Reset"):
        self._username = username
        self._password = passwd
        self._credits = 0
        return None

    def set_username(self, username):
        self._username = username
        return None

    def set_password(self, password):
        self._password = password
        return None

    def add_credits(self, creds):
        self._credits += creds
        return None

    def spend_credits(self, creds):
        self._credits -= creds
        return None

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_credits(self):
        return self._credits
