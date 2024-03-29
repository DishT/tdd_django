from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_methods(self):
        self.assertEqual(1 + 1, 2)

    def test_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))