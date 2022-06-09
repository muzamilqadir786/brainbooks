from django.test import TestCase, SimpleTestCase
from django.urls import reverse



# Create your tests here.
import ipdb
class TestCalls(SimpleTestCase):
    # databases = '__all__'
    def test_call_view_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    #
    # def test_call_view_past_papers(self):
    #     response = self.client.get(reverse('past_papers'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_call_view_generate_paper(self):
    #     response = self.client.get(reverse('generate_paper'))
    #     # self.assertEqual(response.resolver_match.func, 'generate_paper')
    #     # ipdb.set_trace()