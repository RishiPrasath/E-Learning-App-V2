from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from el.models import StatusUpdate

User = get_user_model()


class StatusUpdateViewTests(TestCase):
    def setUp(self):
        # Setup runs before each test method
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        assert self.client.login(username='testuser', password='12345')

    def test_post_status_update(self):
        # Test posting a new status update
        response = self.client.post(reverse('post_status_update'), {'content': 'Posting a new status update'})
        self.assertEqual(response.status_code, 302)  # Assuming the view redirects after a successful post

        # Check if the StatusUpdate was created
        self.assertTrue(StatusUpdate.objects.filter(content='Posting a new status update').exists())

    def test_status_update_page_loads(self):
        # Test loading the page to post a new status update
        response = self.client.get(reverse('post_status_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statusupdate.html')