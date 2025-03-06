import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    """
    Sends an email to the receiver with the given subject and body.

    :param sender_email: Email address of the sender.
    :param sender_password: Password or app-specific password of the sender.
    :param receiver_email: Email address of the receiver.
    :param subject: Subject of the email.
    :param body: Body/content of the email.
    """
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Attach the body to the email
        message.attach(MIMEText(body, "plain"))

        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)  # Log in to the sender's email
            server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


