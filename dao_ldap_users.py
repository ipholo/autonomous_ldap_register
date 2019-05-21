import mysql.connector
import keyring
from autonomous_ldap_register.access_information_module import DatabaseConfiguration


SERVICE_ID = 'LDAP USERS STORAGE'


def connect_to_database():
    return mysql.connector.connect(
        host=DatabaseConfiguration.host,
        user=DatabaseConfiguration.user,
        passwd=DatabaseConfiguration.password,
        database=DatabaseConfiguration.database,
    )


def encrypt_password(username, password):
    keyring.set_password(SERVICE_ID, username, password)
    return keyring.get_password()


def store_ldap_users_information(username, password):
    database_connection = connect_to_database()
    cursor = database_connection.cursor()
    sql_statement = "INSERT INTO users (username, password) VALUES (%s, %s)"
    encrypted_password = encrypt_password(username, password)
    value = (username, encrypted_password)
    cursor.executemany(sql_statement, value)
    database_connection.commit()
    database_connection.close()
