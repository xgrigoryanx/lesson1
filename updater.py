import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def main():
    updater = Updater("326213743:AAFv3ktEuu5RGA8p3hYIcSgJs468sbIISoU")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()
def greet_user(bot, update):
    text = 'Привет!'
    print(text)
    update.message.reply_text(text)
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
main()


