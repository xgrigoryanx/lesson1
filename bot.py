from telegram.ext import Updater
def main():
    updater = Updater("326213743:AAFv3ktEuu5RGA8p3hYIcSgJs468sbIISoU")
    updater.start_polling()
    updater.idle()
main()
