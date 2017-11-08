import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = 'smtp.gmail.com'
SUBJECT = u'A test'
FROM = 'leiger2017@gmail.com'
TO = '1120720058@qq.com'

msg = MIMEMultipart()
msg['From'] = FROM
msg['To'] = TO
msg['Subject'] = SUBJECT

# add main text
msgtext = MIMEText('<p>lol</p><img width="200" src="cid:0">', 'html', 'utf-8')
msg.attach(msgtext)

# add image
with open('./bg.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='bg.jpg')
    # add some necessary information
    mime.add_header('Content-Disposition', 'attachment', filename='bg.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # read the attachment
    mime.set_payload(f.read())
    # encode using base64
    encoders.encode_base64(mime)
    msg.attach(mime)

try:
    server = smtplib.SMTP()
    server.connect(HOST, '587')
    server.starttls()
    # input username and password
    username = input('Username:')
    password = input('Password:')

    server.login(username, password)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print('send mail successfully!')
except Exception as e:
    print('error!', e)
