import smtplib
from autonomous_ldap_register.access_information_module import EmailServerConfiguration, LdapServerConfiguration


# Send an email with the details of the new created server.
def send_ldap_user_email(attributes, full_name, to_email, full_domain_name):
    subject = 'Your user was added to the ldap server.'
    text = 'Hi ' + full_name + '\n\n' \
           + 'Your account has been created in the ldap server: ' + LdapServerConfiguration.FULL_ADMIN_ADDRESS + '.\n' \
           + 'username: ' + attributes['uid'] + '\n' \
           + 'Login DN: ' + full_domain_name + '\n' \
           + 'password: ' + attributes['userPassword'] + '\n\n' \
           + 'Sincerely,\n' \
           + 'Leopoldo Hernandez' \
           + 'Software Engineer'
    server = smtplib.SMTP(EmailServerConfiguration.EMAIL_DOMAIN, 587)
    server.ehlo()
    server.starttls()
    server.login(EmailServerConfiguration.SENDER_EMAIL, EmailServerConfiguration.EMAIL_PASSWORD)
    email_body = '\r\n'.join(['To: %s' % to_email,
                              'From: %s' % EmailServerConfiguration.SENDER_EMAIL,
                              'Subject: %s' % subject,
                              '', text])
    try:
        # This process is blocking the main thread.
        # For improvement this call should be changed to an async call.
        server.sendmail(EmailServerConfiguration.SENDER_EMAIL, [to_email], email_body)
        print('email sent')
    except Exception as e:
        print('error sending mail')
        print(e)
