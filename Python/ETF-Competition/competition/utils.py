# Class defining list of possible permissions of each user
class Permission:
    FULL_ACCESS = 0xff
    STUDENT_ACCESS = 0x01
    PUBLIC_ACCESS = 0x00

    CREATE_COMPETITION = 0x01
    MODIFY_COMPETITION = 0x02
    CREATE_RESULTS = 0x04
    VIEW_RESULTS = 4

def send_email(sender, recipients, subject, template, **kwargs):
    from flask_mail import Message
    msg = Message()