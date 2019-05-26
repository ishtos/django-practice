import os
import re
import json
import time
import datetime

from binance.exceptions import *
from binance.enums import *
from binance.client import Client
from dotenv import load_dotenv

from django.views.generic import TemplateView
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from virtual_currency.models import Currency, CurrencyHistory


# =============================================================================
# Initialize
# =============================================================================
DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)

API_KEY = os.environ.get('API_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

client = Client(API_KEY, SECRET_KEY)


# =============================================================================
# Command
# =============================================================================
class Command(BaseCommand):
    help = 'Delete the specified currency'

    def handle(self, *args, **options):
        # TODO: implementation

        self.stdout.write(self.style.SUCCESS('Successfully delete the specified currency'))
