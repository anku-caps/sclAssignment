import smtplib,ssl
from email.mime.image import MIMEImage
email="mineproject356@gmail.com"
password="1234@robertpattinson"

subject = "Money credited to your account"
body= "Hello, " \
      "we have checked with your bank Mahindra and noticed that 10,000 has been credicted to your account ending with number ****321. Please send the money back immediately to this account. "
message = f'Subject:{subject}\n \n{body}'

reciever = "aspark182@gmail.com"
port = 465
sslcontext = ssl.create_default_context()

connection = smtplib.SMTP_SSL("smtp.gmail.com",port,context=sslcontext)

connection.login(email,password)

for i in range(5):
      connection.sendmail(email, reciever, message)

print("Your message has been delivered")


