import smtplib

def send_email(msg, sender_email, sender_password, recipient_emails):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_emails, msg.as_string())
