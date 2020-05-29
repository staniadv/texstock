import os
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from pathlib import Path

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "lishuy21@gmail.com"  # Enter your address
receiver_emails = ["stas.mc@gmail.com", "aliroman8888@gmail.com"]  # Enter receiver address
password = "Ghjnjrjk_21"

subject = "Этикетки на коробки"
body = "Этикетки во вложенных файлах"


def send_mail(send_from, send_to, subject, message, files=[],
              server="localhost", port=587, username='', password='',
              use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
        msg.attach(part)

    # smtp = smtplib.SMTP(server, port)
    # if use_tls:
    #     smtp.starttls()
    # smtp.login(username, password)
    # smtp.sendmail(send_from, send_to, msg.as_string())
    # smtp.quit()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(send_from, password)
        server.sendmail(send_from, send_to, msg.as_string())


def send_jrpirnt_files():
    files = os.listdir('output')
    files = list(filter(lambda x: (x.endswith('jrprint')), files))
    files = list(map(lambda file: 'output/' + file, files))
    print(files)
    send_mail(sender_email, receiver_emails, subject, body, files,
              smtp_server, port, username='lishuy21', password=password)
