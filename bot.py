import bot_token
import telebot
import _pickle as cPickle


def load_model(filename):
    with open(filename, 'rb') as fid:
        model = cPickle.load(fid)
    return model

PATH_TO_CLF = 'files/NB_classifier.pkl'
PATH_TO_VECTORIZER = 'files/vectorizer.pkl'
PATH_TO_LABEL_ENCODER = 'files/le.pkl'

clf = load_model(PATH_TO_CLF)
vectorizer = load_model(PATH_TO_VECTORIZER)
le = load_model(PATH_TO_LABEL_ENCODER)

bot = telebot.TeleBot(bot_token.token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️. Это твой бот-помощник в твоей студентческой жизни, можешь задавать ему вопросы!")

@bot.message_handler(content_types=["text"])
def process_messages(message):
    data = vectorizer.transform([message.text])
    predict_labels = clf.predict(data)
    response = le.inverse_transform(predict_labels)
    bot.send_message(message.chat.id,response)

if __name__ == '__main__':
    bot.infinity_polling()
