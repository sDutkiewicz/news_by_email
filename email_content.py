import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
import requests

def download_image(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https:' + url
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def create_email_content(popular_news, newest_news):
    email_content = """
    <html>
        <body>
            <h1>Today's Top News</h1>
            <h2>Popular News</h2>
            <ul>
    """

    for article in popular_news:
        email_content += f"""
            <li>
                <h3>{article['title']}</h3>
                <p>{article['lead']}</p>
                <img src="cid:{article['img_src'].split('/')[-1]}" alt="{article['img_alt']}" width="300"><br>
                <a href="{article['link']}">Read more</a>
            </li>
        """

    email_content += """
            </ul>
            <h2>Newest News</h2>
            <ul>
    """

    for article in newest_news:
        email_content += f"""
            <li>
                <h3>{article['title']}</h3>
                <p>{article['lead']}</p>
                <img src="cid:{article['img_src'].split('/')[-1]}" alt="{article['img_alt']}" width="300"><br>
                <a href="{article['link']}">Read more</a>
            </li>
        """

    email_content += """
            </ul>
        </body>
    </html>
    """

    return email_content

def create_email_message(email_content, popular_news, newest_news, sender_email, recipient_emails):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Today's Top News"
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipient_emails)  # Join the list items directly

    part = MIMEText(email_content, 'html')
    msg.attach(part)

    # Attach images
    for article in popular_news + newest_news:
        if article['img_src']:
            img_data = download_image(article['img_src'])
            image = MIMEImage(img_data)
            image.add_header('Content-ID', f"<{article['img_src'].split('/')[-1]}>")
            msg.attach(image)

    return msg


def send_email(msg, sender_email, sender_password, recipient_emails):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_emails.split(','), msg.as_string())
