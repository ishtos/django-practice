import os
from dotenv import load_dotenv

from binance.client import Client

from django.views.generic import TemplateView

# =============================================================================
# init
# =============================================================================
DOTENV_PATH = os.path.join(os.path.dirname(__file__), '.env') 
load_dotenv(DOTENV_PATH)

API_KEY = os.environ.get("API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

client = Client(API_KEY, SECRET_KEY)

# =============================================================================
# view
# =============================================================================
class HomeView(TemplateView):
    template_name = 'virtual_currency/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Currency"
        prices = client.get_all_tickers()
        context["prices"] = prices

        return context
