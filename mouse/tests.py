from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from mouse.models import Block as BlockModel


class PageLoad(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create_user(
            username='test',
            email='test@test.test',
            password='asdf123!'
        )

        self.client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_main_page_load(self) -> None:
        response = self.client.get('/')
        authorized_response = self.authorized_client.get('/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(200, authorized_response.status_code)

    def test_list_of_blocks_load(self) -> None:
        response = self.client.get(reverse('list_of_blocks'))
        authorized_response = self.authorized_client.get(reverse('list_of_blocks'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(200, authorized_response.status_code)

    def test_signup_load(self) -> None:
        response = self.client.get(reverse('reg'))
        authorized_response = self.authorized_client.get(reverse('reg'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(200, authorized_response.status_code)

    def test_account_load(self) -> None:
        response = self.client.get(reverse('profile'))
        authorized_response = self.authorized_client.get(reverse('profile'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(200, authorized_response.status_code)


class SignUp(TestCase):

    def setUp(self) -> None:
        super().setUp()

        self.client = Client()

    def test_signup_valid(self):
        data = {
            'username': 'signup_test',
            'email': 'signup@test.com',
            'password1': 'asdf123!',
            'password2': 'asdf123!'
        }

        response = self.client.post(reverse('reg'), data=data)

        try:
            created_user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            self.fail("Error: could not find created user")

        self.assertEqual(302, response.status_code)
        self.assertEqual(created_user.email, data['email'])

    def test_signup_invalid(self):
        data = {
            'username': 'signup_fail_test',
            'email': 'signup@.com',
            'password1': 'asdf123!',
            'password2': 'asdf123!'
        }

        self.client.post(reverse('reg'), data=data)

        with self.assertRaises(expected_exception=User.DoesNotExist):
            User.objects.get(username=data['username'])


class Block(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create_user(
            username='test_block',
            email='test_block@test.test',
            password='asdf123!'
        )
        self.block = BlockModel.objects.create(
            msg='Саня будет тут',
            nonce=10212390,
            hash='00000039748aee5bd8a69a80fc657fb67585bbfa5b0d681d3982171413daf81e').save()

        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_add_block(self) -> None:
        data = {
            'msg': 'Саня будет там',
            'nonce': 2976321
        }

        response = self.authorized_client.post(reverse('add_block'), data=data)
        try:
            created_block = BlockModel.objects.get(nonce=2976321)
        except BlockModel.DoesNotExist:
            self.fail("Error: could not find created block")
        self.assertEqual(200, response.status_code)
        self.assertEqual(data['msg'], created_block.msg)
        self.assertEqual(data['nonce'], created_block.nonce)