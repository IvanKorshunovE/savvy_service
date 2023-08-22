from django.urls import path
from expense_tracker.views import telegram_webhook

urlpatterns = [
    path("", telegram_webhook, name="telegram_webhook"),
]
