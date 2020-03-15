# smtplib: Simple Mail Transfer Protocol Client
# smtplib includes the class SMTP, which can be used to communicate with mail servers to send mail.

import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

# ----------------------------------
# Sending an Email Message
# The most common use of SMTP is to connect to a mail server and send a message. The mail server
# hostname and port can be passed to the constructor, or connect() can be invoked explicitly. Once
# connected, call sendmail() with the envelope parameters and body of the message. The message
# text should be fully formed and comply with RFC 5322,1 since smtplib does not modify the contents
# or headers at all. That means the From and To headers need to be added by the caller.

# msg = MIMEText("Dear Mr. Mike,\n Thank you for your help. Look forward to talking with you!\nBest,\nAlice")
# msg['To'] = email.utils.formataddr(("Recipient","recipient@example.com"))
# msg['From'] = email.utils.formataddr(("Author","author@example.com"))
# msg["Sugject"] = "Thank you message"

# server = smtplib.SMTP('localhost', 1025)
# server.set_debuglevel(True)

# try:
#     server.sendmail('author@example.com',
#                     ['recipient@example.com'],
#                     msg.as_string())
# finally:
#     server.quit()


# ----------------------------------
# Authentication and Encryption
# The SMTP class also handles authentication and TLS (transport layer security) encryption, when
# the server supports them. To determine whether the server supports TLS, call ehlo() directly to
# identify the client to the server and ask it which extensions are available. Then call has_extn()
# to check the results. After TLS is started, ehlo() must be called again before authenticating
# the user. Many mail hosting providers now support only TLS-based connections. For communicating
# with those servers, use SMTP_SSL to initiate an encrypted connection.


servername = "smtp.office365.com"
serverport = 587
if serverport:
    serverport = int(serverport)
else:
    serverport = 25

use_tls = input("Use TLS? (yes/no): ").lower()
to_email = input("Recipient: ")
username = input("Mail username: ")
password = getpass.getpass("%s's password: " % username)

msg = MIMEText(
    "Dear Mr. Mike,\n\n    Thank you for your help. Attached please find my resume. Look forward to talking with you!\n\nBest,\nKai"
)
msg.set_unixfrom("Alice")
msg["To"] = email.utils.formataddr(("Recipient", to_email))
msg["From"] = email.utils.formataddr(("Kai", username))
msg["Subject"] = "Summer Intern Application"

if use_tls == "yes":
    print("starting with a secure connection")
    server = smtplib.SMTP_SSL(servername, serverport)
else:
    print("starting with an insecure connection")
    server = smtplib.SMTP(servername, serverport)
try:
    server.set_debuglevel(True)
    server.ehlo()
    if server.has_extn("STARTTLS"):
        print("(starting TLS)")
        server.starttls()
        server.ehlo()
    else:
        print("(no STARTTLS)")
    if server.has_extn("AUTH"):
        print("(logging in)")
        server.login(username, password)
    else:
        print("(no AUTH)")
    server.sendmail(username, [to_email], msg.as_string())

finally:
    server.quit()
