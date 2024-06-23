from parse import fetch_and_parse

def extract_info(soup, section_selector, item_selector, title_selector, exclude_domain=None):
    section = soup.select_one(section_selector)
    if not section:
        print(f"Section {section_selector} not found")
        return []

    items = section.select(item_selector)
    articles = []

    for item in items:
        link = item['href']
        if exclude_domain and exclude_domain in link:
            continue

        title_tag = item.select_one(title_selector)
        title = title_tag.get_text(strip=True) if title_tag else "No title available"
        linked_soup = fetch_and_parse(link)
        
        lead_div = linked_soup.find('div', class_='hyphenate lead')
        main_photo = linked_soup.find('figure', class_='mainPhoto')
        
        lead_text = lead_div.get_text(strip=True) if lead_div else "No description available"
        img_tag = main_photo.find('img') if main_photo else None
        img_src = img_tag['src'] if img_tag else None
        img_alt = img_tag.get('alt', 'No description available') if img_tag else "No description available"

        if img_src and img_src.startswith('//'):
            img_src = 'https:' + img_src

        articles.append({
            'title': title,
            'lead': lead_text,
            'img_src': img_src,
            'img_alt': img_alt,
            'link': link
        })

        print(articles)
    
    return articles
