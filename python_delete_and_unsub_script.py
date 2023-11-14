import webbrowser
import imaplib
import bs4
import email
from email.header import decode_header

# Required Config for Gmail accounts.
# Others, please look up the documentation....
imaplib._MAXLINE = 10000000
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT ='993'

imap = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

# Added the lines here to take your user input for email and password
email_id = input('Enter your Email-ID: ')
password = input('Enter your Password: ')

# This logs you in to your mail-account.
imap.login(email_id, password)

try:
    _, data = imap.select('INBOX', readonly=True) # if you don't want to check the INBOX folder, replace 'INBOX' with the folder you need (if it's a subfolder of a folder like "[Gmail]", put '[Gmail]/<folder to scan>')
    num_msgs = int(data[0])
    # print(num_msgs)
    # You can print it to see how many mails you have

    _, search_data =imap.search(None, 'SINCE "11-NOV-2023"') # you can replace 'ALL' with... see examples here: https://www.thepythoncode.com/article/deleting-emails-in-python

    for nums in search_data[0].split():
        # The mails have to fetched in the RFC822 format, or others.. you can look up :)
        _, data = imap.fetch(nums, '(RFC822)')
        _, b = data[0]
        email_msg = email.message_from_bytes(b)
        for part in email_msg.walk():   # loop for going thorugh all the mails
            if part.get_content_type() == 'text/html':
                body = part.get_payload(decode=True)   # get the body of the mail
                soup = bs4.BeautifulSoup(body, 'lxml')   
                links = soup.findAll('a')       # get all links in an email
                for selected in links:     # loop for checking unsub
                    if 'unsubscribe' in selected.text.lower(): # you can add other strings with the "or" operator
                        webbrowser.open(selected.get('href'))
except Exception as e:
    print(e)

print("Delete e-mails since that date? [y/N]", end=" ")
while (input() != 'y' and input() != 'N'): # no support for capital (uppercase) "y" and lowercase "n", sorry :/
    print("Sorry. Try again.\nDelete e-mails since that date? [y/N]")
if input() == 'y':
    
    _, data = imap.select('INBOX', readonly=True) # if you don't want to check the INBOX folder, replace 'INBOX' with the folder you need (if it's a subfolder of a folder like "[Gmail]", put '[Gmail]/<folder to scan>')
    num_msgs = int(data[0])
    # print(num_msgs)
    # You can print it to see how many mails you have

    _, search_data =imap.search(None, 'FROM <email-address@provider.domain>', 'SINCE "11-NOV-2023"') # you can replace 'ALL' with... see examples here: https://www.thepythoncode.com/article/deleting-emails-in-python

    # convert messages to a list of email IDs (I put another try and another split because I was unsure whether this is necessary for deleting e-mails or not. Probably not, but better safe than sorry.)
    messages = search_data[0].split(b' ')

    for mail in messages:
        _, msg = imap.fetch(mail, "(RFC822)")
        # you can delete the for loop for performance if you have a long list of emails
        # because it is only for printing the SUBJECT of target email to delete
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # if it's a bytes type, decode to str
                    subject = subject.decode('latin-1') # default is 'utf-8'
                print("Deleting", subject)
        # mark the mail as deleted
        imap.store(mail, "+FLAGS", "\\Deleted")

# permanently remove mails that are marked as deleted
# from the selected mailbox (in this case, INBOX)
imap.expunge()
# close the mailbox
imap.close()
# logout from the account
imap.logout()