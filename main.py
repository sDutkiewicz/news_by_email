import os
from extract import extract_info, fetch_and_parse
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
    sender_email = os.getenv('EMAIL_USER')
    sender_password = os.getenv('EMAIL_PASS')
    recipient_emails = os.getenv('RECIPIENT_EMAILS').split(',')

    # Create and send email
    msg = create_email_message(email_content, popular_news, newest_news, sender_email, recipient_emails)
    send_email(msg, sender_email, sender_password, recipient_emails)

if __name__ == "__main__":
    job()
