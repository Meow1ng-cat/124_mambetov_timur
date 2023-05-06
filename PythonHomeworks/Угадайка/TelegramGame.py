import random
import telebot
import os
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=['start'])
def startgame(start):
    secretnumber = random.randint(1, 100)
    move_counter = 0
    bot.send_message(start.chat.id, "Угадайте число!")

    def game():
        @bot.message_handler(content_types=["text"])
        def chechnumber(message):
            nonlocal secretnumber
            nonlocal move_counter
            try:
                allegednumber = int(message.text)
            except ValueError:
                bot.send_message(message.chat.id, "Введите целое число")
                game()
                return 0
            if allegednumber < 1 or allegednumber > 100:
                bot.send_message(message.chat.id, "Введите число от 1 до 100")
                game()
                return 0
            if secretnumber > allegednumber:
                bot.send_message(message.chat.id, "Загаданное число больше")
                move_counter += 1
                game()
                return 0
            elif secretnumber < allegednumber:
                bot.send_message(message.chat.id, "Загаданное число меньше")
                move_counter += 1
                game()
                return 0
            else:
                move_counter += 1
                bot.send_message(message.chat.id, "Поздравляю вы угадали число! Ваше количетво попыток:")
                bot.send_message(message.chat.id, str(move_counter))
                secretnumber = random.randint(1, 100)
                move_counter = 0

    game()


bot.polling()
