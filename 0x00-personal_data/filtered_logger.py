#!/usr/bin/env python3
"""Contains a function that returns the log message obfuscated."""
import logging
import re
import os
import mysql.connector
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records using `filter_datum`.
        """
        record.msg = filter_datum(self.fields, RedactingFormatter.REDACTION,
                                  record.msg, RedactingFormatter.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Function that returns the log message obfuscated."""
    obfuscated_str: str = message
    for field in fields:
        obfuscated_str = re.sub('{}=.*?(?={})'.format(field, separator),
                                '{}={}'.format(field, redaction),
                                obfuscated_str)
    return obfuscated_str


def get_logger() -> logging.Logger:
    """
    Function that creates a Logger object and obfuscates the appropriate
    data.
    """
    new_logger: logging.Logger = logging.getLogger('user_data')
    new_logger.setLevel(logging.INFO)
    new_logger.propagate = False
    handler: logging.StreamHandler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    new_logger.addHandler(handler)
    return new_logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Function that returns a connector to a MySQL database."""
    return mysql.connector.\
        connect(user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
                password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
                host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
                database=os.getenv('PERSONAL_DATA_DB_NAME')
                )


def main() -> None:
    """
    Main function to retrieve all rows in a database and display each row in
    a filtered format.
    """
    logger = get_logger()
    db: mysql.connector.connection.MySQLConnection = get_db()
    cursor = db.cursor()

    query = ("SELECT * FROM users;")

    cursor.execute(query)
    users = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    for user in users:
        user_dict = dict(zip(field_names, user))
        user_str = RedactingFormatter.SEPARATOR.join(
            f"{key}={value}" for key, value in user_dict.items()
        )
        logger.info(user_str)

    db.close()


if __name__ == '__main__':
    main()
