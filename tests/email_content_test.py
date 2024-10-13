import unittest
from email_content import create_email_content

class TestCreateEmailContent(unittest.TestCase):

    def test_create_email_content(self):
        popular_news = [
            {
                "title": "Popular News 1",
                "lead": "Lead text for popular news 1",
                "img_name": "img1.jpg",
                "img_alt": "Image 1",
                "link": "http://example.com/news1"
            }
        ]
        newest_news = [
            {
                "title": "Newest News 1",
                "lead": "Lead text for newest news 1",
                "img_name": "img2.jpg",
                "img_alt": "Image 2",
                "link": "http://example.com/news2"
            }
        ]

        email_content = create_email_content(popular_news, newest_news)

        # Check if generated HTML includes the expected news
        self.assertIn("Popular News 1", email_content)
        self.assertIn("Newest News 1", email_content)
        self.assertIn("img1.jpg", email_content)
        self.assertIn("img2.jpg", email_content)

if __name__ == "__main__":
    unittest.main()
