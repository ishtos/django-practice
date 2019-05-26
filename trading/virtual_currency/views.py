import os
import re
import time
import json
import datetime
from dotenv import load_dotenv

from binance.client import Client
from binance.enums import *
from binance.exceptions import *

from django.utils import timezone
from django.views.generic import TemplateView

from .models import Currency, CurrencyHistory

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

        balance = client.get_asset_balance(asset='BTC')
        context['balance'] = balance

        now = datetime.datetime.now()
        week_ago = now - datetime.timedelta(days=7)
        context['klines'] = client.get_historical_klines('ETHBTC', Client.KLINE_INTERVAL_1DAY, week_ago.strftime('%d %b, %Y'), now.strftime('%d %b, %Y'))
        
        # tickers = client.get_ticker()
        # for ticker in tickers:
        #     if 'BTC' in ticker['symbol']:
        #         currencyHistory = CurrencyHistory(symbol=str(ticker['symbol']))
        #         currencyHistory.save()

        #         currency = Currency(
        #             currency_history=currencyHistory,
        #             symbol=str(ticker['symbol']), 
        #             price_change_percent=float(ticker['priceChangePercent']), 
        #             weighted_avg_price=float(ticker['weightedAvgPrice']), 
        #             volume=float(ticker['volume']), 
        #             count=float(ticker['count']), 
        #             saved_date=timezone.now())
        #         currency.save()

        balance = client.get_asset_balance(asset='BTC')
        context['asset'] = balance['asset']
        context['free'] = balance['free']
        context['locked'] = balance['locked']

        context['now'] = datetime.datetime.now()
        context['up_currency'] = Currency.objects.order_by('price_change_percent')[:5]
        context['down_currency'] = Currency.objects.order_by('-price_change_percent')[:5]


        return context
