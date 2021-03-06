import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
sg = SendGridAPIClient(SENDGRID_API_KEY)


def send_mail(to_emails, subject, html_content):
    message = Mail(
        from_email="Coliv'app <admin@30emeciel.fr>",
        to_emails=to_emails,
        subject=subject,
        html_content=html_content)

    response = sg.send(message)
    assert response.status_code == 202
    return response


if __name__ == "__main__":
    send_mail("Tony <tony.lbvre@gmail.com>", "Test email", "<strong>hello World!</strong>")

