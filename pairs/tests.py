from django.test import TestCase

# Create your tests here.
class dummy(TestCase):
    def setUp(self):
        x = 1
        y = 2

    def test_dummy(self):
        self.assertEqual(1, 1)
