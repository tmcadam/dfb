from django.test import TestCase, Client


class RootTestCase(TestCase):

    def test_root_url_returns_200_and_Helloworld(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello World - Basic pipeline working')
