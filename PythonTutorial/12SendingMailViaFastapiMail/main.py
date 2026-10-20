from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
import uvicorn


app = FastAPI()

# 1. Use this config if you want to use the fastapi mails with the sendGrid,by using this approach the main send successfully but it will go inside the spam folder because you are not using the custom or business email.
# import os
# import certifi
# import ssl
# os.environ['SSL_CERT_FILE'] = certifi.where()
# ssl_context = ssl.create_default_context(cafile=certifi.where())
# conf = ConnectionConfig(
#     MAIL_USERNAME="apikey",   # your email
#     MAIL_PASSWORD="",      # Gmail app password or SendGrid key
#     MAIL_FROM="sahilkumar32755@gmail.com",       # same as MAIL_USERNAME
#     MAIL_PORT=587,
#     MAIL_SERVER="smtp.sendgrid.net",                # or smtp.sendgrid.net if using SendGrid SMTP
#     MAIL_STARTTLS=True,
#     MAIL_SSL_TLS=False,
#     USE_CREDENTIALS=True,
#     VALIDATE_CERTS=True
# )

# 2. Use this config if you wanna to use the fastapi Mail with the google app passoword,this email are not store in the spam folder:
conf = ConnectionConfig(
    MAIL_USERNAME="sahilkumar32755@gmail.com",
    MAIL_PASSWORD="nsbvgwosjepssjqz",
    MAIL_FROM="sahilkumar32755@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


class EmailSchema(BaseModel):
    email: EmailStr


@app.post("/send-email")
async def send_email(background_tasks: BackgroundTasks, body: EmailSchema):
    message = MessageSchema(
        subject="FastAPI-Mail Test",
        recipients=[body.email],  # List of recipients
        body="<b>Hello, this is a test email from FastAPI-Mail!</b>",
        subtype="html",
    )

    fm = FastMail(conf)
    # Here we add the work in the queue so that it will start working after sending the response.You can also use await at that point.
    background_tasks.add_task(fm.send_message, message)
    return {"status": "Email has been sent to " + body.email}


if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
