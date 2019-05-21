# Autonomous Ldap Register
Python application to register users to an Open LDAP server and a database, and notify 
 the user by email through a csv file.

## Getting Started

This following packages must be installed to run locally the application.

```
pip install ldap3
```

```
pip install mysql-connector-python
```

```
pip install Flask
```
In the [Access Information Module](https://github.com/ipholo/autonomous_ldap_register/blob/master/access_information_module.py) 
the information of the connections must be configured.

## How it Works
After installing the required modules, and the access information module is
configured, you can run the application with the command:

```
python app.py
```

This will start a web application where you can upload a CSV file with the format:
```
(first name, last name, email)
```

After uploading a file, the application will create a user in the specified Open Ldap Server of each entry
by creating a username and a password.
 
* Username: Partial first name and last name with two random numbers in lowercase.
* Password. Random 8 characters whit letters in uppercase, lowercase, numbers and simbols

After the user creation an email (the specified in the csv file)
will be sent to the new created user with the username and the password. Finally, the username and password will be 
stored in the specified database.

## Authors

* **Leopoldo Hernandez** - *Software Engineer* - [Personal Site](http://ipolo.tech)

