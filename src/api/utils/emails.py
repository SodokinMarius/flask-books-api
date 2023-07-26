from flask_mail import Message, Mail


from flask import current_app

mail = Mail()


def send_email(to, subject, template):
    print("Envoi email")
    print("mail_default ",current_app.config.get('MAIL_DEFAULT_SENDER'))
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=current_app.config.get('MAIL_DEFAULT_SENDER')
    )
    # print("Mon message ####",msg)

    mail.send(msg)