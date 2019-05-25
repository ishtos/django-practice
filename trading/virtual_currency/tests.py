from .models import Currency
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Currency


class CurrencyModelTests(TestCase):
    def test_saved_within_a_week_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future = Currency(saved_date=time)
        self.assertIs(future.saved_within_a_week(), False)

    def test_saved_within_a_week_past(self):
        time = timezone.now() - datetime.timedelta(days=7, seconds=1)
        past = Currency(saved_date=time)
        self.assertIs(past.saved_within_a_week(), False)

    def test_saved_within_a_week_recent(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent = Currency(saved_date=time)
        self.assertIs(recent.saved_within_a_week(), True)
