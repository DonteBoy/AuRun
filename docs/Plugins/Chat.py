from string import punctuation
import nltk
import re
import json
import random
import time
from colorama import Fore
from numpy import average, vectorize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# admin = f"Donte"
# bot_name = f"AuRun"
# intro = f"----------Chat----------"
# chat_bot_say = f"\nВремя\nПогоду\nЗадачи на сегодня"
# chat_bot_make = f"\nОткрыть (Приложение / Страничку в браузере)\nСкачать видео с YouTube"
# info = f"{Fore.WHITE}Вот что Я могу\n{Fore.CYAN}Сказать: {Fore.WHITE}{chat_bot_say}\n{Fore.CYAN}Сделать: {Fore.WHITE}{chat_bot_make}"


# print(time.strftime('%H'))
# print(intro)
# print(info)

go = print("go")

config_file = open("docs/big_bot_config.json", "r")
BOT_CONFIG = json.load(config_file)

x = []
y = []

vectorizer = CountVectorizer()
vectorizer.fit(x)
x_vectorized = vectorizer.transform(x)

model = LogisticRegression()
model.fit(x_vectorized, y)

test = vectorizer.transform([""])
model.predict(test)

# BOT_CONFIG = {
#     "intents": {
#         "hello": {
#             "examples": ["Привет","Ага"],
#             "responses": ["Привет", "Йоу"]
#         },
#         "bye": {
#             "examples": ["Пока"],
#             "responses": ["Пока"]
#         }
#     },
#     "intents_def": {
#         "Время": {
#             "examples": ["Время",""],
#             "responses": f"{go}"
#         },
#         "Погода": {
#             "examples": ["Погода",""],
#             "responses": f"{go}"
#         },
#         "Задачи на сегодня": {
#             "examples": ["Задачи на сегодня",""],
#             "responses": f"{go}"
#         },
#         "Открыть приложение": {
#             "examples": ["Открыть приложение",""],
#             "responses": f"{go}"
#         },
#         "Открыть страничку в браузере": {
#             "examples": ["Открыть страничку в браузере",""],
#             "responses": f"{go}"
#         },
#         "Скачать видео с YouTube": {
#             "examples": ["Скачать видео с YouTube",""],
#             "responses": f"{go}"
#         },
#     },
#     "censored": {
#         "examples": ["Блядь","Ебать","Бля","Хуй","Ебало","Ебаш","Сука","Придор"],
#         "responses": ["-_-","Извинись !","Сам такой !"]
#     },
#     "failure_phrases": ["Что ?","Я ничего не понял !","Я всего лишь бот !","Что Ты от Меня хочешь ?","Повтори", "-_- ?"]
# }


def normalize(text):
    text = text.lower()
    punctuation = r"[^\w\s]"
    return re.sub(punctuation, "", text)

def isMatching(text1, text2):
    text1 = normalize(text1)
    text2 = normalize(text2)
    distance = nltk.edit_distance(text1,text2)
    average_length = (len(text1) + len(text2))
    return distance / average_length < 0.4

def getIntent(text):
    all_intents = BOT_CONFIG["intents"]
    for name, data in all_intents.items():
        for example in data["examples"]:
            if isMatching(text, example):
                return name

def getAnswer(intent):
    responses = BOT_CONFIG["intents"][intent]["responses"]
    return random.choice(responses)

def bot(text):
    intent = getIntent(text)
    if not intent:
        pass
    if intent:
        return getAnswer(intent)
    # intents_def = BOT_CONFIG[intents_def][""]
    # return random.choice(intents_def)
    failure_phrases = BOT_CONFIG["failure_phrases"]
    return random.choice(failure_phrases)

for name, data in BOT_CONFIG["intents"].items():
    for example in data["examplae"]:
        x.append(example)
        y.append(name)


# for pair in database:
#     if isMatching(question, pair["question"]) < 0.4:
#         answer = random.choice(pair["answer"])
#         print(answer)

