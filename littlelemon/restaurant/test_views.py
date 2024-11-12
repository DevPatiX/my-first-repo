from django.test import TestCase
from .models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):

    def setUp(self):
        # Add a few instances of Menu to the database for testing
        Menu.objects.create(title="Burger", price=50, inventory=200)
        Menu.objects.create(title="Pizza", price=120, inventory=150)

        # Set up user and token
        self.user = User.objects.create_user(username='DevPatiX', password='PaTi@2002')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_get_all(self):
        # Send a GET request to the URL for retrieving the Menu items (replace 'menu-list' with your URL name)
        response = self.client.get(reverse('menu'))  # Adjust the view name

        # Assert that the response status is OK (200)
        self.assertEqual(response.status_code, 200)

        # Check that the serialized data matches the response
        menu_items = Menu.objects.all()
        expected_data = [
            { 'id': item.id, 'title': item.title, 'price': str(item.price), 'inventory': item.inventory} for item in menu_items
        ]
        self.assertEqual(response.json(), expected_data)
