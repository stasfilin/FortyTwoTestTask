from django.test.testcases import TestCase
from django.core.urlresolvers import reverse

from apps.hello.models import Persons


class IndexTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_create_model(self):
        Persons.objects.create(first_name='Stanislav',
                               last_name='Filin',
                               date='1994-04-20',
                               bio='Chernivtsi City',
                               email='stasfilinmusic@gmail.com',
                               jabber='stasfilin@qutim.org',
                               skype='stas_filin',
                               other='Telegram: @stasfilin'
                               )
        self.assertEqual(bool(Persons.objects.filter(first_name='Stanislav', last_name='Filin')), True)

    def test_admin_login(self):
        data = {
            'name': 'admin',
            'password': 'admin'
        }
        response = self.client.post(reverse('admin:index'), data)
        self.assertEqual(response.status_code, 200)