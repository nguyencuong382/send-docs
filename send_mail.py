import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils import load_json

CONFIG_PATH = 'credentials.json'


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def send(message, subject):
    names, emails = get_contacts('contacts.txt')  # read contacts

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()

    global CONFIG_PATH
    email_credentials = load_json(CONFIG_PATH)
    s.login(email_credentials['email'], email_credentials['app_password'])

    # For each contact, send the email:
    for name, email in zip(names, emails):
        print(f'Seding email to {email}')
        msg = MIMEMultipart()       # create a message

        # setup the parameters of the message
        msg['From'] = email_credentials['email']
        msg['To'] = email
        msg['Subject'] = subject

        # add in the message body
        msg.attach(MIMEText(message, 'html'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()
