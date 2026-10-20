from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.core.config import getenv

# print(getenv.MAIL_USER);
# print(getenv.MAIL_PASS);

conf = ConnectionConfig(
    MAIL_USERNAME=getenv.MAIL_USER,
    MAIL_PASSWORD=getenv.MAIL_PASS,
    MAIL_FROM=getenv.MAIL_USER,
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


async def send_reset_email(email: str, token: str):
    reset_link = f"https://your-frontend-app.com/reset-password?token={token}"

    message = MessageSchema(
        subject="Password Reset",
        recipients=[email],  # list of recipients
        body=f"""
        <div style="font-family: Arial, sans-serif; color:#333;">
            <h1>Password Reset Request</h1>
            <p>Click the button below to reset your password. 
            This link will expire in <strong>5 minutes</strong>.</p>

            <a href="{reset_link}" 
            style="display:inline-block; padding:12px 20px; margin:20px 0;
                    background-color:#2E86C1; color:#fff; text-decoration:none;
                    font-size:16px; border-radius:5px;">
            Reset Password
            </a>

            <p>If the button above doesn’t work, copy and paste this link into your browser:</p>
            <p><a href="{reset_link}">click here</a></p>
        </div>
        """,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)