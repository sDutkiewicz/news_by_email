from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
import requests

def download_image(url, name):
    response = requests.get(url)
    response.raise_for_status()
    img_data = BytesIO(response.content).read()
    img_name = name.split('/')[-1]
    return img_data, img_name

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
                <img src="cid:{article['img_name']}" alt="{article['img_alt']}" width="300"><br>
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
                <img src="cid:{article['img_name']}" alt="{article['img_alt']}" width="300"><br>
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

    alternative_part = MIMEMultipart('alternative')
    part = MIMEText(email_content, 'html')
    alternative_part.attach(part)
    msg.attach(alternative_part)

    for article in popular_news + newest_news:
        if article['img_src']:
            img_data, img_name = download_image(article['img_src'], article['img_name'])
            image = MIMEImage(img_data)
            image.add_header('Content-ID', f"<{img_name}>")
            image.add_header('Content-Disposition', 'inline', filename=img_name)
            msg.attach(image)

    return msg
