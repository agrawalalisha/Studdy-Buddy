from django.test import TestCase
from studdybuddy.forms import ProfileForm


class ProfileForm(TestCase):
    def test_empty_form(self):
        form = ProfileForm()
        self.assertInHTML(
            '<input type="text" name="date" required id="id_date">', str(form)
        )
        self.assertInHTML(
            '<input type="text" name="due_date" required id="id_due_date">', str(form)
        )