import unittest
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]

class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.tags = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

class PortfolioAcceptance(unittest.TestCase):
    def test_complete_bilingual_pages_and_downloads(self):
        for language, name in [('fr', 'index.html'), ('en', 'en/index.html')]:
            with self.subTest(language=language):
                page = ROOT / name
                self.assertTrue(page.exists(), f'Missing {language} page')
                doc = Document(page.read_text())
                self.assertIn(('html', {'lang': language}), doc.tags)
                self.assertEqual(sum(tag == 'h1' for tag, _ in doc.tags), 1)
                self.assertFalse(any(tag == 'form' for tag, _ in doc.tags))
                ids = [a['id'] for _, a in doc.tags if 'id' in a]
                self.assertEqual(len(ids), len(set(ids)))
                for section in ['services', 'experience', 'approach', 'contact']:
                    self.assertIn(section, ids)
                links = [a for tag, a in doc.tags if tag == 'a']
                pdfs = {a['href'] for a in links if 'download' in a}
                self.assertEqual(len(pdfs), 2)
                self.assertTrue(any(a.get('href') == 'https://www.linkedin.com/in/domichel/' for a in links))
                for tag, a in doc.tags:
                    for attr in ['href', 'src']:
                        url = a.get(attr, '')
                        if not url or urlparse(url).scheme or url.startswith('//'):
                            continue
                        path = unquote(urlparse(url).path)
                        fragment = urlparse(url).fragment
                        if not path:
                            if fragment: self.assertIn(fragment, ids)
                            continue
                        target = (page.parent / path).resolve()
                        self.assertTrue(target.is_relative_to(ROOT))
                        self.assertTrue(target.exists(), f'Broken resource: {url}')
                        if target.suffix == '.pdf':
                            self.assertTrue(target.read_bytes().startswith(b'%PDF'))

if __name__ == '__main__':
    unittest.main()
