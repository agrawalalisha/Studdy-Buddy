from django.test import SimpleTestCase, TestCase, Client, RequestFactory
from chat.views import all_rooms
from studdybuddy.forms import ProfileForm, ProfileViewForm
from studdybuddy.models import Profile, Course
from django.urls import reverse
from django.contrib.auth.models import User
from .views import *

class TestProfileForm(SimpleTestCase):
    def test_empty_form(self):
        form = ProfileForm(data={})
        self.assertFalse(
            form.is_valid()
        )
        self.assertIn(
            "last_name", form.fields
        )

    def test_filled_form(self):# SHOULD BE TRUE except for courses.
        form = ProfileForm(data={
            "first_name": "Tester",
            "last_name": "Graham",
            "email": "email@yahoo.com",
            "pronouns": "they/them",
            "year": "Second Year",
            "major": "computer science",
            "bio": "i'm happy"
        })
        self.assertTrue(form.is_valid())

class TestProfileViewForm(SimpleTestCase):
    def test_empty_form(self):
        form = ProfileViewForm(data={})
        self.assertFalse(
            form.is_valid()
        )
        self.assertIn(
            "last_name", form.fields
        )

    def test_filled_form(self):# SHOULD BE TRUE except for courses.
        form = ProfileViewForm(data={
            "first_name": "Tester",
            "last_name": "Graham",
            "email": "email@yahoo.com",
            "pronouns": "they/them",
            "year": "Second Year",
            "major": "computer science",
            "bio": "i'm happy"
        })
        self.assertTrue(form.is_valid())

client = Client()
class TestUrls(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='user', email='email@yahoo.com', password='pw')
        self.profile = Profile.objects.create(email="email@yahoo.com")
    
    def test_all_rooms(self):
        request = self.factory.get('/dashboard')
        request.user = self.user
        response = all_rooms(request)
        self.assertEqual(response.status_code,200)

    def test_dashboard(self):
        request = self.factory.get('/dashboard')
        request.user = self.user
        response = dashboard_view(request)
        self.assertEqual(response.status_code,200)

    def test_code_of_conduct(self):
        request = self.factory.get('/dashboard')
        request.user = self.user
        response = code_of_conduct_view(request)
        self.assertEqual(response.status_code,200)

    def test_create_profile(self):
        response = self.client.get('/create_profile/')
        self.assertEqual(response.status_code,200)

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)

    def test_view_profile(self):
        request = self.factory.get('/dashboard/')
        request.user = self.user
        response = profile_list(request)
        self.assertEqual(response.status_code,200)

    def test_edit_profile(self):
        request = self.factory.get('/dashboard/')
        request.user = self.user
        response = edit_profile_view(request)
        self.assertEqual(response.status_code,200)

    def test_edit_classes(self):
        request = self.factory.get('/dashboard/')
        request.user = self.user
        response = edit_classes_view(request)
        self.assertEqual(response.status_code,200)
    
    def test_profile_list(self):
        request = self.factory.get('/dashboard/')
        request.user = self.user
        response = edit_profile_view(request)
        self.assertEqual(response.status_code,200)

    def test_forum(self):
        request = self.factory.get('/dashboard/')
        request.user = self.user
        response = forum(request)
        self.assertEqual(response.status_code,200)

    def test_sessions(self):
        request = self.factory.get('/dashboard/')
        request.user = self.user
        response = sessions_view(request)
        self.assertEqual(response.status_code,200)

    def test_nonexistent_url(self):
        response = self.client.get("/no/")
        self.assertEqual(response.status_code,404)


