from django.test import TestCase
from .models import Menu

class MenuItemTest(TestCase):
    
    def test_get_item(self):
        # Create an instance of the Menu model
        item = Menu.objects.create(title="IceCream", price=8, inventory=50)
        
        # Test that the string representation is as expected
        self.assertEqual(str(item), "IceCream : 8")
