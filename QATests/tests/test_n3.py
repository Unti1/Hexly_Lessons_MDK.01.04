import pytest


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
@pytest.fixture(scope='module')
def user():
    return User(
        username="testuser",
        password="testpassword"
    )
    
def test_user_creation(user):
    assert user.username == "testuser"
    assert user.password == "testpassword"

def test_user_password_channged(user):
    user.password = "newpassword"
    assert user.password == "newpassword"
    
def test_user_password_after_change(user):
    assert user.password == "newpassword"
    