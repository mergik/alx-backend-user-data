#!/usr/bin/env python3
""" Test file should return no output"""
import requests


def register_user(email: str, password: str) -> str:
    """ Test registering new user """
    data = {
        "email": email,
        "password": password
    }
    response = requests.post('localhost:5000/users', json=data)
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """ Test logging in with wrong password """
    data = {
        "email": email,
        "password": 'wrongPW'
    }
    response = requests.post('localhost:5000/sessions', json=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Test logging in with correct password """
    data = {
        "email": email,
        "password": password
    }
    response = requests.post('localhost:5000/sessions', json=data)
    assert response.status_code == 200


def profile_unlogged() -> None:
    """ Test profile unlogged - no session ID """
    data = {
        "session_id": ""
    }
    response = requests.get('localhost:5000/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """ Test profile logged """
    data = {
        "session_id": session_id
    }
    response = requests.get('localhost:5000/profile', json=data)
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """ Test log out accurately """
    data = {
        "session_id": session_id
    }
    response = requests.delete('localhost:5000/sessions', json=data)
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """ Test retrieving reset password token """
    data = {
        "email": email
    }
    response = requests.post('localhost:5000/reset_password', json=data)
    assert response.status_code == 200


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Test updating password """
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put('localhost:5000/reset_password', json=data)
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
