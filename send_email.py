import smtplib

def send_email(message, sender_email, sender_password, recipient_email):
    # Send the email via Gmail's SMTP server
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, recipient_email, message.as_string())
    smtp.quit()
