from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating new user with email is successfull """
        email = 'test@gmail.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test email for new user is normalized """
        email = 'Test@gmaiL.com'

        user = get_user_model().objects.create_user(
            email,
            'password'
        )

        first, sep, domain = email.partition('@')
        domain = domain.lower()
        email = first + sep + domain
        self.assertEqual(user.email, email)

    def test_create_new_superuser(self):
        """Test Creatign a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
