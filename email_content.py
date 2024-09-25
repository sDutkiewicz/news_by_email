from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from io import BytesIO
import requests
from mimetypes import guess_type
from requests.exceptions import RequestException

def download_image(url, name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = response.content
        
        # Attempt to get MIME type from response headers
        content_type = response.headers.get('Content-Type')
        if not content_type:
            # Fall back to guessing from file extension
            mime_type, encoding = guess_type(name)
            content_type = mime_type or 'application/octet-stream'
        
        img_name = name.split('/')[-1]
        img_extension = content_type.split('/')[-1]

        return img_data, img_name, img_extension
    except RequestException as e:
        print(f"Error downloading image from {url}: {e}")
        return None, None, None

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
            img_data, img_name, img_extension = download_image(article['img_src'], article['img_name'])
            
            if img_data:
                # Create MIMEImage with the correct image type
                image = MIMEImage(img_data, _subtype=img_extension)
                image.add_header('Content-ID', f"<{img_name}>")
                image.add_header('Content-Disposition', 'inline', filename=img_name)
                msg.attach(image)
            else:
                print(f"Skipping image for {article['title']} due to download issues.")

    return msg
