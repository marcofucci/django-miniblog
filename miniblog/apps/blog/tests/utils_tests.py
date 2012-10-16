from django.test import TestCase

from blog.utils import get_annotated_authors, get_annotated_tags, \
    get_annotated_categories


class UtilsTestCase(TestCase):
    fixtures = ['posts.json']

    def test_get_annotated_authors(self):
        authors = get_annotated_authors()
        self.assertEqual(
                [(author.username, author.post_count) for author in authors], 
                [('marcofucci', 2), ('johndoe', 1)]
            )

    def test_get_annotated_tags(self):
        tags = get_annotated_tags()
        self.assertEqual(
                [(tag.slug, tag.post_count) for tag in tags], 
                [('music', 2), ('signing', 1), ('fun', 1), ('rock', 1), ('blues', 1)]
            )

    def test_get_annotated_categories(self):
        categories = get_annotated_categories()
        self.assertEqual(
                [(category.slug, category.post_count) for category in categories], 
                [('music', 2), ('fun', 1)]                
            )