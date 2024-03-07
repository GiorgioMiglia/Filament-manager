import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Filament


class FilamentModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_purchase = Filament(purchase_date=time)
        self.assertIs(future_purchase.was_purchased_recently(), False)