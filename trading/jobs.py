import subprocess
import schedule
import time

# =============================================================================
# jobs
# =============================================================================
def update_currency():
    cmd = 'python manage.py update_currency.py'
    subprocess.Popen(cmd.split())


def delete_currency():
    cmd = 'python manage.py delete_currency.py'
    subprocess.Popen(cmd.split())

# =============================================================================
# scheduler
# =============================================================================
schedule.every().day.at("00:00").do(update_currency)
schedule.every().day.at("12:00").do(update_currency)

schedule.every().sunday.at("12:00").do(delete_currency)

while True:
    schedule.run_pending()
    time.sleep(60)
