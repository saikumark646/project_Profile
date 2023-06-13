from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status


# Create your tests here.


class ProfileAPITestCase(TestCase):

    def test_create_profile(self):
        url ='http://127.0.0.1:8000/user_create/'
        data = {'email': 'test@example.com', 'first_name': 'suresh', 'last_name': 'kumar','password':'suresh'}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(email=data.get('email'))
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.first_name, 'suresh')
        self.assertEqual(user.last_name, 'kumar')

