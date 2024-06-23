from io import BytesIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests

def download_image(url):
    response = requests.get(url)
    return BytesIO(response.content)

def create_email_content(popular_articles, newest_articles):
    email_content = """
    <html>
        <body>
            <h1>Today's Top News</h1>
            <h2>Popular News</h2>
            <ul>
    """

    for article in popular_articles:
        if article['img_src']:
            email_content += f"""
                <li>
                    <h3>{article['title']}</h3>
                    <p>{article['lead']}</p>
                    <img src="cid:{article['img_src'].split('/')[-1]}" alt="{article['img_alt']}" width="300"><br>
                    <a href="{article['link']}">Read more</a>
                </li>
            """
        else:
            email_content += f"""
                <li>
                    <h3>{article['title']}</h3>
                    <p>{article['lead']}</p>
                    <p>No image available</p>
                    <a href="{article['link']}">Read more</a>
                </li>
            """

    email_content += """
            </ul>
            <h2>Newest News</h2>
            <ul>
    """

    for article in newest_articles:
        if article['img_src']:
            email_content += f"""
                <li>
                    <h3>{article['title']}</h3>
                    <p>{article['lead']}</p>
                    <img src="cid:{article['img_src'].split('/')[-1]}" alt="{article['img_alt']}" width="300"><br>
                    <a href="{article['link']}">Read more</a>
                </li>
            """
        else:
            email_content += f"""
                <li>
                    <h3>{article['title']}</h3>
                    <p>{article['lead']}</p>
                    <p>No image available</p>
                    <a href="{article['link']}">Read more</a>
                </li>
            """

    email_content += """
            </ul>
        </body>
    </html>
    """

    return email_content


def create_email_message(email_content, popular_articles, newest_articles, sender_email, recipient_email):
    msg = MIMEMultipart('related')
    msg['Subject'] = "Today's Top News"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    part = MIMEText(email_content, 'html')
    msg.attach(part)

    for article in popular_articles + newest_articles:
        if article['img_src']:
            image_data = download_image(article['img_src'])
            img = MIMEImage(image_data.read())
            img.add_header('Content-ID', f"<{article['img_src'].split('/')[-1]}>")
            img.add_header('Content-Disposition', 'inline', filename=article['img_src'].split('/')[-1])
            msg.attach(img)

    return msg
