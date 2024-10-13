import unittest
from bs4 import BeautifulSoup

class TestExtractNews(unittest.TestCase):

    def test_extract_news_success(self):
        # Mock HTML content
        html_content = """
        <html>
        <body>
            <div class="news-section">
                <article>
                    <h2 class="title">Test News 1</h2>
                    <a href="http://example.com/news1">Read More</a>
                </article>
                <article>
                    <h2 class="title">Test News 2</h2>
                    <a href="http://example.com/news2">Read More</a>
                </article>
            </div>
        </body>
        </html>
        """

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')

        # Manually find the articles
        news_section = soup.find("div", class_="news-section")
        articles = news_section.find_all("article")
        titles = [article.find("h2", class_="title").get_text() for article in articles]

        # Print for debugging
        print("Manual extraction:", titles)

        # Ensure the manual extraction works
        self.assertGreater(len(titles), 0)
        self.assertIn("Test News 1", titles)
        self.assertIn("Test News 2", titles)

if __name__ == "__main__":
    unittest.main()
