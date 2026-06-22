import pytest

#N1 --------------------------------------------

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9 / 5) + 32
#
# def test_freezing_point():
#     assert celsius_to_fahrenheit(0) == pytest.approx(32.0)
#
# def test_boiling_point():
#     assert celsius_to_fahrenheit(100) == pytest.approx(212.0)
#
# def test_negative_temperature():
#     assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)

#N2 ---------------------------------------------------------

# def check_password(users, username, password):
#     if username not in users:
#         raise ValueError(f'User {username} does not exist')
#
#     if users[username] != password:
#         raise ValueError(f'User {username} does not match password')
#
#     return True

#N3 ----------------------------------------------------------

def is_valid(email):
    return '@' in email and '.' in email

@pytest.mark.parametrize(
    "email, expected",
    [
        ("test@example.com", True),
        ("user@mail.ge", True),
        ("hello.world@gmail.com", True),
        ("testexample.com", False),
        ("test@com", False),
        ("@gmail.com", False),
        ("user@", False),
        ("plaintext", False),
    ]
)
def test_email_validation(email, expected):
    assert is_valid(email) == expected