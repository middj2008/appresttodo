from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('deji','middj2008@gmail.com','password123@!')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'middj2008@gmail.com')


    def test_creates_super_user(self):
        user = User.objects.create_superuser('deji','middj2008@gmail.com','password123@!')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'middj2008@gmail.com')


    def test_raises_value_when_no_username_supply(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email='middj2008@gmail.com',password='password123@!')


    def test_raises_error_with_message_when_no_username_supply(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='middj2008@gmail.com',password='password123@!')


    def test_raises_value_when_no_email_supply(self):
        self.assertRaises(ValueError, User.objects.create_user, username="username", email='',password='password123@!')


    def test_raises_error_with_message_when_no_email_supply(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='username', email='',password='password123@!')


    def test_cant_create_super_user_with_not_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='', email='middj2008@gmail.com',password='password123@!',is_staff=False)


    def test_cant_create_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='', email='middj2008@gmail.com',password='password123@!',is_superuser=False)
        

    