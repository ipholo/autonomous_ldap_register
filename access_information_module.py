# File to store sensitive information. This file should not be in plain text
# in production.


# Information of the open ldap server.
# The default domain component. Currently using my own domain: ipolo.tech
# The default user where users are going to be stored.
# common name = admin
# Password to enter the server.
# The default structure used in the hosted open ldap server.
# The default gid number of an existing group.
# The default home directory in the ldap server.
class LdapServerConfiguration:
    IP_ADDRESS = ''
    DOMAIN_COMPONENT = ''
    USER = ''
    PASSWORD = ''
    DIRECTORY_STRUCTURE = ['inetOrgPerson', 'posixAccount', 'top']
    GID_NUMBER = 500
    HOME_DIRECTORY = '/home/users/'
    FULL_ADMIN_ADDRESS = ''


# Information of the ldap server.
# Sender email which will be sending email.
# SMTP domain to send email.
# Account password.
class EmailServerConfiguration:
    SENDER_EMAIL = ''
    EMAIL_DOMAIN = 'smtp.gmail.com'
    EMAIL_PASSWORD = ''


# Information to access the database.
# Currently using a mysql Instance.
class DatabaseConfiguration:
    host = 'localhost'
    user = 'yourusername'
    password = 'yourpassword'
    database = 'database'
