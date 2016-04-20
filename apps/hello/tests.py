from django.test.testcases import TestCase
from django.core.urlresolvers import reverse


class IndexTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

