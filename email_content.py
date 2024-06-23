from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
import requests

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
    msg = MIMEMultipart('related')
    msg['Subject'] = "Today's Top News"
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipient_emails)

    part = MIMEText(email_content, 'html')
    msg.attach(part)

    def download_image(url):
        response = requests.get(url)
        return BytesIO(response.content)

    for article in popular_news + newest_news:
        if article['img_src']:
            img_data = download_image(article['img_src'])
            image = MIMEImage(img_data.read())
            image.add_header('Content-ID', f"<{article['img_src'].split('/')[-1]}>")
            msg.attach(image)

    return msg
