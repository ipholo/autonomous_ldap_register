import csv
from ldap_module import add_ldap_user


# Function to read a csv file with the format:
# first name, last name, email
# And call the call ldap user function
def read_csv_file(filename):
    with open(filename, newline='', mode='r', encoding='utf-8-sig') as csv_file:
        users_list = csv.reader(csv_file, delimiter=',', quotechar='|')
        for user in users_list:
            first_name = user[0]
            last_name = user[1]
            email = user[2]
            # This function could be changed to async as
            # it currently blocks.
            print(add_ldap_user(first_name, last_name, email))
