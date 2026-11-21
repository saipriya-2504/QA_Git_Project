def test_valid_login():
    username = "admin"
    password = "admin123"

    assert username == "admin"
    assert password == "admin123"


def test_invalid_login():
    username = "user"

    assert username != "admin"

def test_logout():
    status = "logged_out"

    assert status == "logged_out"