from parse import fetch_and_parse

def extract_info(soup, section_class, link_class, title_class, exclude_domain=None):
    items = soup.select(f"{section_class} {link_class}")
    articles = []

    for item in items:
        link = item['href']
        if exclude_domain and exclude_domain in link:
            continue

        title = item.select_one(title_class).get_text(strip=True)
        linked_soup = fetch_and_parse(link)
        lead_div = linked_soup.find('div', class_='hyphenate lead')
        main_photo = linked_soup.find('figure', class_='mainPhoto')
        
        lead_text = lead_div.get_text(strip=True) if lead_div else "No description available"
        img_src = main_photo.find('img')['src'] if main_photo and main_photo.find('img') else None
        img_alt = main_photo.find('img').get('alt', 'No description available') if img_src else "No description available"

        articles.append({
            'title': title,
            'lead': lead_text,
            'img_src': img_src,
            'img_alt': img_alt,
            'link': link
        })

    return articles
