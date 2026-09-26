import json
import re
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET
from test_site import Document

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://milkshek.github.io/mdo-consultech/'

class SEOAcceptance(unittest.TestCase):
    def test_canonical_language_graph_and_identity(self):
        for lang, file, url in [('fr', 'index.html', SITE), ('en', 'en/index.html', SITE + 'en/')]:
            with self.subTest(lang=lang):
                source = (ROOT / file).read_text()
                tags = Document(source).tags
                self.assertEqual([a['href'] for t, a in tags if t == 'link' and a.get('rel') == 'canonical'], [url])
                alternates = {a['hreflang']: a['href'] for t, a in tags if t == 'link' and a.get('rel') == 'alternate'}
                self.assertEqual(alternates, {'fr': SITE, 'en': SITE + 'en/', 'x-default': SITE})
                structured = re.search(r'<script type="application/ld\+json">(.*?)</script>', source, re.S)
                self.assertIsNotNone(structured)
                graph = json.loads(structured.group(1))['@graph']
                page = next(item for item in graph if item['@type'] == 'WebPage')
                self.assertEqual(page['url'], url)
                self.assertEqual(page['inLanguage'], lang)
                person = next(item for item in graph if item['@type'] == 'Person')
                self.assertEqual(person['name'], 'Michel Do')
                self.assertIn('https://github.com/Milkshek', person['sameAs'])
                self.assertIn('https://www.linkedin.com/in/domichel/', person['sameAs'])
                self.assertNotIn('aggregateRating', source)
                self.assertFalse(any(t == 'meta' and 'noindex' in a.get('content', '') for t, a in tags))

    def test_sitemap_contains_only_canonical_pages(self):
        path = ROOT / 'sitemap.xml'
        self.assertTrue(path.exists(), 'Missing sitemap')
        tree = ET.parse(path)
        urls = [item.text for item in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        self.assertEqual(urls, [SITE, SITE + 'en/'])

if __name__ == '__main__':
    unittest.main()
