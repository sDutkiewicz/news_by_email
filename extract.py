from bs4 import BeautifulSoup
import requests

def fetch_and_parse(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def extract_info(soup, section_class, article_selector, title_selector, exclude_domain=None):
    items = soup.select(f"{section_class} {article_selector}")
    articles = []

    for item in items:
        link = item['href']
        if exclude_domain and exclude_domain in link:
            continue

        title = item.select_one(title_selector).get_text(strip=True)
        linked_soup = fetch_and_parse(link)
        lead_div = linked_soup.find('div', class_='hyphenate lead')
        main_photo = linked_soup.find('figure', class_='mainPhoto')
        
        lead_text = lead_div.get_text(strip=True) if lead_div else "No description available"
        img_src = main_photo.find('img')['src'] if main_photo and main_photo.find('img') else None
        img_alt = main_photo.find('img').get('alt', 'No description available') if img_src else "No description available"
        img_name = img_src.split('/')[-1] if img_src else "no_image"

        articles.append({
            'title': title,
            'lead': lead_text,
            'img_src': f"https:{img_src}" if img_src.startswith("//") else img_src,
            'img_alt': img_alt,
            'img_name': img_name,
            'link': link
        })

    return articles
