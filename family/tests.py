from django.test import TestCase ,RequestFactory

# Create your tests here.
from models import *


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.last_name = 'Lennon'
        user.save()

    def test_register_already_available_user(self):
        usr_data = {'username':'john','email_id':'averma@loggly.com'}
        URL = '/family/register/'
        resp = self.client.post(URL, usr_data)
        self.assertEqual(resp.status_code ,200)

    def test_new_user_register(self):
        usr_data = {'username': 'ashish', 'email_id': 'averma@loggly.com'}
        URL = '/family/register/'
        resp = self.client.post(URL, usr_data)
        self.assertTemplateUsed(resp, 'signup.html')

    def test_login_present_user(self):
        usr_data = {'username': 'john', 'password': 'johnpassword'}
        URL = '/family/login/'
        resp = self.client.post(URL, usr_data)
        self.assertRedirects(resp,'/login/getdata',target_status_code = 302)

    def test_login_unknown_user(self):
        usr_data = {'username': 'jraohn', 'password': 'ndmdn'}
        URL = '/family/login/'
        resp = self.client.post(URL, usr_data)
        self.assertEqual(resp.status_code,501)

