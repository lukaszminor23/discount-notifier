from email.message import EmailMessage
import ssl
import smtplib


def send_mail():
    email_sender = 'Senders email address'
    email_password = 'Senders email app password'
    email_receiver = 'Receivers email address'

    subject = 'Item is on sale'
    body = '''
    Desired item is currently on sale.
    https://8a.pl/buty-do-rakow-polautomatycznych-scarpa-ribelle-lite-hd-tonic-tonic
    '''

    email = EmailMessage()
    email['From'] = email_sender
    email['To'] = email_receiver
    email['Subject'] = subject
    email.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, email.as_string())
