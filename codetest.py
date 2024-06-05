import unittest
from main import Spider

class TestSpider(unittest.TestCase):

    def test_crawl(self):
        spider = Spider("https://coder.today")
        spider.crawl()
        self.assertEqual(len(spider.data), 50)  # Check if data is not bigger than 50 pages

    def test_extract_urls(self):
        spider = Spider("https://coder.today")
        urls = spider.extract_urls("https://coder.today")
        self.assertEqual(len(urls), 10)  # Check if 10 URLs are extracted

        for url in urls:
            self.assertTrue(url.startswith("https://coder.today/"))  # Check if extracted URLs have the correct format


if __name__ == '__main__':
    unittest.main()