from openmicnight.user import User

def test_user_defaults():
    username = "my_user"
    newUser = User(username)
    assert newUser.get_username() == username
    assert newUser.get_password() == "Reset"
    assert newUser.get_credits() == 0

def test_user_username():
    username = "my_user"
    new_username = "new_username"
    newUser = User(username)
    assert newUser.get_username() == username
    newUser.set_username(new_username)
    assert newUser.get_username() == new_username

def test_user_password():
    username = "my_user"
    new_password = "new_password"
    newUser = User(username)
    assert newUser.get_password() == "Reset"
    newUser.set_password(new_password)
    assert newUser.get_password() == new_password

def test_user_credits():
    username = "my_user"
    password = "password"
    new_credits = 50
    spend_credits = 25
    newUser = User(username, password)
    assert newUser.get_credits() == 0
    newUser.add_credits(new_credits)
    assert newUser.get_credits() == new_credits
    newUser.spend_credits(spend_credits)
    assert newUser.get_credits() == spend_credits
    

