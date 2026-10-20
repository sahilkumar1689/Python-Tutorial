import certifi
import ssl
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# print(ssl.get_default_verify_paths())
# ssl._create_default_https_context = ssl._create_unverified_context

message = Mail(
    from_email='sahilkumar32755@gmail.com',
    to_emails='tempuse55555555@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')


def send_via_sendgrid():
    try:
        # Force Python to use certifi’s CA bundle
        os.environ['SSL_CERT_FILE'] = certifi.where()
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        # sg.set_sendgrid_data_residency("eu")
        # uncomment the above line if you are sending mail using a regional EU subuser
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
        
        
if __name__ == "__main__":
    send_via_sendgrid();


