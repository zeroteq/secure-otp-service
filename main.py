import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_otp(email, otp):
    # Get Gmail credentials from environment variables
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv("GMAIL_ADDRESS")  # Get email address from environment variable
    password = os.getenv("GMAIL_APP_PASSWORD")  # Get app-specific password from environment variable
    receiver_email = email  # The recipient's email address

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Your OTP Code"

    # Email body with the OTP
    body = f"Your OTP code is {otp}"
    message.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)  # Log in using app-specific password
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send email
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

# Usage: Call the function to send an OTP to a recipient
send_otp("recipient@example.com", "1234")
