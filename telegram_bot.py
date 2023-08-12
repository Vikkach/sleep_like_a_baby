import os
import telebot
from chat_bot import context, collect_messages

bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))


@bot.message_handler(commands=['start'])
def start(msg):
    info = """
    Hello! I'm your AI baby sleep coach, how can I help you today?
    """

    bot.send_message(msg.chat.id, info)

    messages = context.copy()

    @bot.message_handler(content_types=['text'])
    def send_text(msg):
        message = msg.text
        response = collect_messages(message, messages)
        bot.send_message(msg.chat.id, response)


if __name__ == "__main__":
    bot.infinity_polling()
