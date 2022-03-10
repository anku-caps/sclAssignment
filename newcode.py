import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = "mineproject356@gmail.com"
Reciever_Email = ["aspark182@gmail.com","mineproject356@gmail.com"]
Password = input('Enter your email account password: ')


newMessage = EmailMessage()
newMessage['Subject'] = "Check out the new program PDF"
newMessage['From'] = Sender_Email
newMessage['To'] = Reciever_Email
newMessage.set_content('we have checked with your bank Mahindra and noticed that 10,000 has been credicted to your account ending with number ****321. Please send the money back immediately to this account.')

files = ['index.html']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password)
    for i in range(5):
     smtp.send_message(newMessage)