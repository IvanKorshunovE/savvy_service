import telebot
from django.conf import settings
from django.db.models import Sum

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from expense_tracker.models import Expense

bot_token = settings.TOKEN
bot = telebot.TeleBot(bot_token)

COMMANDS = (
    "/start - почати використання бота\n"
    "/help - отримати допомогу з використанням\n"
    "/expenses - отримати загальну суму витрат"
)


def send_message_with_commands(message, text):
    bot.reply_to(message, f"{text}\n\n{COMMANDS}")


@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        json_str = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "invalid request"})


@bot.message_handler(commands=["start"])
def handle_start(message):
    send_message_with_commands(
        message,
        "Ласкаво просимо до Expense Tracker бота! "
        "Будь ласка введіть сумму та короткий опис розділяючи їх пробілами."
    )


@bot.message_handler(commands=["help"])
def handle_help(message):
    send_message_with_commands(
        message,
        "Будь ласка введіть сумму та короткий опис розділяючи їх пробілами."
    )


@bot.message_handler(commands=["expenses"])
def handle_expenses(message):
    user_id = message.from_user.id
    total_expense = Expense.objects.filter(
        user_id=user_id
    ).aggregate(
        total_amount=Sum("amount")
    ).get("total_amount")

    if total_expense:
        total_expense_str = str(round(total_expense, 2))
        send_message_with_commands(
            message,
            f"Ваші загальні витрати становлять {total_expense_str} грн."
        )
    else:
        send_message_with_commands(message, "Щось пішло не так.")


@bot.message_handler(func=lambda message: True)
def handle_expense(message):
    try:
        user_id = message.from_user.id
        amount, description = message.text.split(maxsplit=1)
        expense = Expense(
            amount=amount, description=description, user_id=user_id
        )
        expense.save()
        bot.reply_to(message, "Витрати успішно додано!")
    except Exception as e:
        bot.reply_to(
            message,
            "Щось пішло не так. Будь ласка спробуйте ще раз. "
            "Переконайтесь що ви ввели сумму та короткий "
            "опис розділяючи їх пробілами"
        )


WEBHOOK_URL = settings.WEBHOOK_URL
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)
