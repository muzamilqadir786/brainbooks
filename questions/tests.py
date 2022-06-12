import os
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth.models import User



import ipdb
class QuestionViewsTestCalls(TestCase):
    fixtures = ['boards.json', 'classes.json', 'subjects.json', 'chapters.json', 'topics.json']
    # fixtures = [os.path.join('/brainbooks/fixtures/',fixture) for fixture in fixtures]

    def setUp(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    def test_call_view_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_call_view_generate_paper(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/questions/generate-paper/')
        self.assertEqual(response.status_code, 200)
        ipdb.set_trace()

    def test_call_view_free_mcqs_test(self):
        response = self.client.get('/questions/free-mcqs/')
        self.assertEqual(response.status_code, 200)

    def test_call_view_past_papers(self):
        response = self.client.get('/questions/past-papers/')
        self.assertEqual(response.status_code, 200)



    # def test_call_view_past_papers(self):
    #     response = self.client.get(reverse('past_papers'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_call_view_generate_paper(self):
    #     response = self.client.get(reverse('generate_paper'))
    #     # self.assertEqual(response.resolver_match.func, 'generate_paper')
    #     # ipdb.set_trace()