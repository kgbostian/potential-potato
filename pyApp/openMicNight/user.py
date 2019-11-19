class User:
    def __init__(self, username, passwd="Reset"):
        self._username = username
        self._password = passwd
        self._credits = 0
        return None

    def setUsername(self, username):
        self._username = username
        return None

    def setPassword(self, password):
        self._password = password
        return None

    def addCredits(self, creds):
        self._credits += creds
        return
