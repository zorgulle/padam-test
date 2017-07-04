from django.test import TestCase
from django.test import Client
>>> from django.core.urlresolvers import reverse

# Create your tests here.
class TestHomeView(TestCase):
    """Test home view
    """

    def set_up(self):
        """
        Set up is call before each test
        """

        self.client = Client()
    def test_response_200(self):
        """
        Test that the view is not in error
        :return:
        """
        expected = 200
        response = self.client.get(reverse('booking_list'))

        self.AssertEqual(response.code, expected)
