from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMessage
import os

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# help to send email
class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            from_email = os.environ.get("Email_FROM"),
            to=[data['to_email']]
        )
        email.send()