from django.test import TestCase
from restaurant.models import Menu
from django.core import serializers

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
        
class MenuViewTest(TestCase):
    def setup(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
    def test_getall(self):
        menus = Menu.objects.all()
        item_json = serializers.serialize('json', menus)
        self.assertEqual(menus, item_json)