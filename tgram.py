from telegram.ext import Updater, CommandHandler
import subprocess


def status(bot, update):
    # we use subprocess because of matplotlib's memory leak 
    # when using several savefig
    subprocess.call(['python', 'plot.py'])
    chat_id = update.message.chat_id
    print(f"request from {chat_id}")
    bot.send_photo(chat_id=chat_id, photo=open('status.png', 'rb'))


def main():
    TOKEN = "put your awesome token here, just go to @BotFather"
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('status', status))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
