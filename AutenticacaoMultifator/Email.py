import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = "smtp.gmail.com"
port = 587
username = "omega.marcos@gmail.com"
password = "wmfyltpowarwepto"


def enviar_email(code):
    mail_from = "omega.marcos@gmail.com"
    mail_to = "marcos@omegasistemas.com.br"
    mail_subject = "Código E-mail"
    mail_body = "Código de validação: %d " % code

    msg = MIMEMultipart()
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Subject'] = mail_subject
    msg.attach(MIMEText(mail_body, 'plain'))

    connection = smtplib.SMTP(server, port)
    connection.starttls()
    connection.login(username, password)
    connection.send_message(msg)
    connection.quit()



