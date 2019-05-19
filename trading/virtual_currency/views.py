import os
import re
import time
import json
from dotenv import load_dotenv
from datetime import datetime

from binance.client import Client
from binance.enums import *
from binance.exceptions import *

from django.views.generic import TemplateView

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
class HomeView(TemplateView):
    template_name = 'virtual_currency/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        prices = client.get_all_tickers()
        context['prices'] = prices

        return context

class BalanceView(TemplateView):
    template_name = 'virtual_currency/balance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        balance = client.get_asset_balance(asset='BTC')
        context['asset'] = balance['asset']
        context['free'] = balance['free']
        context['locked'] = balance['locked']

        return context