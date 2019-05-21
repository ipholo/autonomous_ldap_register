from access_information_module import LdapServerConfiguration
from email_sender_module import send_ldap_user_email
from ldap3 import Server, Connection, ALL
from random import randint


# Function to generate username.
# The first tree letters of first name and last name are used.
# Two random number are added for redundancy.
def generate_user_id(first_name, last_name):
    random_number = str(randint(10, 99))
    if len(first_name) > 3:
        first_name = first_name[0: 3]
    if len(last_name) > 3:
        last_name = last_name[0: 3]
    return (first_name + last_name + random_number).lower()


# 8 length generator password based on ascii characters from 33 to 122
# which includes letters (uppercase & lowercase), numbers and symbols.
def generate_password():
    password = ''
    for i in range(8):
        random_number = randint(33, 122)
        password = password + chr(random_number)
    return password


# Function to generate the new ldap user attributes.
def generate_attributes(first_name, last_name):
    generated_user_id = generate_user_id(first_name, last_name)
    return {
        'uid': generated_user_id,
        'uidNumber': 1,
        'sn': last_name,
        'gidNumber': LdapServerConfiguration.GID_NUMBER,
        'homeDirectory': LdapServerConfiguration.HOME_DIRECTORY + generated_user_id,
        'userPassword': generate_password(),
    }


# Function to create a new ldap user based on its first name and last name.
def add_ldap_user(first_name, last_name, email):
    server = Server(LdapServerConfiguration.IP_ADDRESS, get_info=ALL)
    conn = Connection(server, LdapServerConfiguration.USER, LdapServerConfiguration.PASSWORD, auto_bind=True)
    attributes = generate_attributes(first_name, last_name)
    cn = attributes['uid']
    full_domain_name = 'cn=' + cn + ',' + LdapServerConfiguration.DOMAIN_COMPONENT
    was_added = conn.add(full_domain_name, LdapServerConfiguration.DIRECTORY_STRUCTURE, attributes)
    if not was_added:
        print('The following user was not added: ' + cn)
        print(conn.result)
    else:
        send_ldap_user_email(attributes, cn, email, full_domain_name)
    conn.unbind()
    return was_added
