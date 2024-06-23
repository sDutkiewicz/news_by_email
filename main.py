import os
from parse import fetch_and_parse
from extract import extract_info
from email_content import create_email_content, create_email_message
from send_email import send_email

def job():
    url = "https://wiadomosci.onet.pl/"
    soup = fetch_and_parse(url)

    # Extract Popular News
    print("Extracting Popular News...")
    popular_news = extract_info(soup, 'section.widgetFeed', 'li a', 'div.popularNewsTitle')

    # Extract Newest News
    print("Extracting Newest News...")
    newest_news = extract_info(soup, 'div.wdgBests.boxWrapper', 'a.mediumNewsBox.lpsItem', 'h3.title span', 'csr.onet.pl')

    # Compile email content
    email_content = create_email_content(popular_news, newest_news)

    # Email settings
    sender_email = os.getenv('EMAIL')
    sender_password = os.getenv('EMAIL_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    # Create and send email
    msg = create_email_message(email_content, popular_news, newest_news, sender_email, recipient_email)
    send_email(msg, sender_email, sender_password, recipient_email)

if __name__ == "__main__":
    job()
