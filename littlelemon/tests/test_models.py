from django.test import TestCase
from restaurent.models import MenuItem, Booking


class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEquals(item, "IceCream : 80")
