#!/usr/bin/env python3
"""
Contains a `hash_password` fn that returns a salted,
hashed password, which is a byte string
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Takes in a password string and returns
    a salted, hashed password, which is a byte string
    """
    encoded_password = password.encode('utf-8')
    return (bcrypt.hashpw(encoded_password, bcrypt.gensalt()))


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates the provided password to the hashed password"""
    encoded_password = password.encode('utf-8')
    if bcrypt.checkpw(encoded_password, hashed_password):
        return True
    return False
