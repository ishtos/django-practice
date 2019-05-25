import os
import re
import time
import json
from dotenv import load_dotenv
from datetime import datetime

from binance.client import Client
from binance.enums import *
from binance.exceptions import *

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Currency

# =============================================================================
# init
# =============================================================================
DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env') 
load_dotenv(DOTENV_PATH)

API_KEY = os.environ.get('API_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

client = Client(API_KEY, SECRET_KEY)

# =============================================================================
# view
# =============================================================================
class IndexView(TemplateView):
    model = Currency
    template_name = 'virtual_currency/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        prices = client.get_all_tickers()
        # context['prices'] = prices
        for price in prices:
            if 'BTC' in price['symbol']:
                context[price['symbol']] = price['price']

        # klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")

        # info = client.get_exchange_info()
        # context['info'] = info

        balance = client.get_asset_balance(asset='BTC')
        context['balance'] = balance

        status = client.get_account_status()
        context['status'] = status

        tickers = client.get_ticker()
        for ticker in tickers:
            if 'BTC' in ticker['symbol']:
                Currency(
                    symbol=str(ticker['symbol']), 
                    priceChangePercent=float(ticker['priceChangePercent']), 
                    weightedAvgPrice=float(ticker['weightedAvgPrice']), 
                    volume=float(ticker['volume']), 
                    count=float(ticker['count']), 
                    saved_date=timezone.now()).save()

        balance = client.get_asset_balance(asset='BTC')
        context['asset'] = balance['asset']
        context['free'] = balance['free']
        context['locked'] = balance['locked']

        context['now'] = datetime.now()

        context['up_currency'] = Currency.objects.order_by('priceChangePercent')[:5]
        context['down_currency'] = Currency.objects.order_by('-priceChangePercent')[:5]


        return context
    
    def get_queryset(self):
        return Currency.objects.order_by('priceChangePercent')
