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
    help = 'Update each currency information'

    def handle(self, *args, **options):
        tickers = client.get_ticker()
        for ticker in tickers:
            if 'BTC' in ticker['symbol']:
                currencyHistory = CurrencyHistory(symbol=str(ticker['symbol']))
                currencyHistory.save()

                currency = Currency(
                    currency_history=currencyHistory,
                    symbol=str(ticker['symbol']),
                    price_change_percent=float(ticker['priceChangePercent']),
                    weighted_avg_price=float(ticker['weightedAvgPrice']),
                    volume=float(ticker['volume']),
                    count=float(ticker['count']),
                    saved_date=timezone.now())
                currency.save()

        self.stdout.write(self.style.SUCCESS('Successfully update each currency informatio'))

