
import smtplib
from email.mime.text import MIMEText
from typing import Dict

class EmailSender:
    def __init__(self, smtp_server: str, port: int, email: str, password: str):
        self.smtp_server = smtp_server
        self.port = port
        self.email = email
        self.password = password

    def send(self,to_email: str, subject: str, content: str):

        body = f"""
        """
        
        msg = MIMEText(body)
        msg["Subject"] = "Daily Campaign Report"
        msg["From"] = self.email
        msg["To"] = to_email
        
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.port) as server:  # Use SMTP_SSL for port 465
                server.login(self.email, self.password)
                server.sendmail(self.email, to_email, content)
                print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")


































# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Configure email
# sender_email = "your_email@gmail.com"
# password = "your_password"
# receiver_email = "recipient@example.com"
# subject = "Hello from Python"
# body = "This is a test email sent via Python."

# # Create message
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject
# message.attach(MIMEText(body, "plain"))

# # Send email
# try:
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # Use SMTP_SSL for port 465
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message.as_string())
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Error: {e}")