import bot_token
import telebot

PATH_TO_CLF = './classifier.pkl'
PATH_TO_VECTORIZER = './vectorizer.pkl'
PATH_TO_LABEL_ENCODER = './le.pkl'

bot = telebot.TeleBot(bot_token.token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️. Это твой бот-помощник в твоей студентческой жизни, можешь задавать ему вопросы!")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
