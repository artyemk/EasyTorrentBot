from bs4 import BeautifulSoup
import urllib
import re
import telebot
from urllib.parse import quote
import os.path
import requests
from telebot import types

token = "443707456:AAEqKmYuSLwvU30eAKs7VfwxcTbVd0kXTt0"
bot = telebot.TeleBot(token)
url = "https://api.telegram.org/bot%s/",token
markup = types.ReplyKeyboardMarkup()
markup.row('/start','/game','/base')
markup.row('/info','/feedback')

SwitchTracker = 0
Name = []
Choise = 0
mesg = ''
# proxies = {
#   'http': '177.141.157.4',
#   'https': '177.141.157.4',
# }
#
# requests.get('tfile.co', proxies=proxies)
@bot.message_handler(commands=['1'])
def first(mes):
    global Choise
    Choise = 1
    if SwitchTracker == 0:
        GetHtml(mesg)
        bot.send_message(mesg.chat.id, "Ок, лови")
        bot.send_document(mes.chat.id, open('/home/usr/Desktop/torrent.torrent', 'rb'))
        Choise = 0
        Name.clear()
        os.remove("/home/usr/Desktop/torrent.torrent")
    elif SwitchTracker == 1:
        GetGamehtml(mesg)
        bot.send_message(mesg.chat.id, "Ок, лови")
        bot.send_document(mes.chat.id, open('/home/usr/Desktop/game.torrent', 'rb'))
        Choise = 0
        Name.clear()
        os.remove("/home/usr/Desktop/game.torrent")
@bot.message_handler(commands=['2'])
def second(mes):
    global Choise
    Choise = 2
    if SwitchTracker == 0:
        GetHtml(mesg)
        bot.send_message(mesg.chat.id, "Ок, лови")
        bot.send_document(mes.chat.id, open('/home/usr/Desktop/torrent.torrent', 'rb'))
        Choise = 0
        Name.clear()
        os.remove("/home/usr/Desktop/torrent.torrent")
    elif SwitchTracker == 1:
        GetGamehtml(mesg)
        bot.send_message(mesg.chat.id, "Ок, лови")
        bot.send_document(mes.chat.id, open('/home/usr/Desktop/game.torrent', 'rb'))
        Choise = 0
        Name.clear()
        os.remove("/home/usr/Desktop/game.torrent")
@bot.message_handler(commands=['3'])
def second(mes):
    global Choise
    Choise = 3
    if SwitchTracker == 0:
        GetHtml(mesg)
        bot.send_message(mesg.chat.id, "Ок, лови")
        bot.send_document(mes.chat.id, open('/home/usr/Desktop/torrent.torrent', 'rb'))
        Choise = 0
        Name.clear()
        os.remove("/home/usr/Desktop/torrent.torrent")
    elif SwitchTracker == 1:
        GetGamehtml(mesg)
        bot.send_message(mesg.chat.id, "Ок, лови")
        bot.send_document(mes.chat.id, open('/home/usr/Desktop/game.torrent', 'rb'))
        Choise = 0
        Name.clear()
        os.remove("/home/usr/Desktop/game.torrent")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, ты попал на канал торрент бота 😏 \n"
                                      "Игровой трекер: /game \n" +
                                      "Базовый трекер: /base \n"
                                      "Инфо о боте: /info \n"
                                      "Как пользоваться: /howto\n"
                                      "Оставить отзыв: /feedback" ,reply_markup=markup)
@bot.message_handler(commands=['howto'])
def info(message):
    bot.send_message(message.chat.id,'Искать нужную вам информацию можно по нескольким трекерам, которые активируются с помощью комманд /base и /game \n'
                                     '/base - обычный трекер, на котором можно найти много полезного\n'
                                     '/game - трекер для игр, так что игрушки качаем с помощью этой команды, хотя можно попробовать и с /base\n'
                                     'Писать нужно именно то, что вам нужно. Без лишней инфы, ибо бот ищет торренты по вашим ключевым словам\n'
                                     'В будущем будут добавляться новые трекеры. Если у вас есть любимый - пишите мне, возможно добавлю 😎')
@bot.message_handler(commands=['base'])
def base(message):
    global SwitchTracker
    SwitchTracker = 0
    bot.send_message(message.chat.id, "Чего качаем?")
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Данный бот проводит анализ крупнейших торрент трекеров в России, вытаскивая только нужную вам информацию \n"
                                      "Сейчас бот находится в стадии тестирования, так что возможны перебои в работе\n"
                                      "Если есть замечания по поводу работы бота или какие-либо советы, то пишите либо в /feedback, либо лично мне: https://vk.com/trick540")
@bot.message_handler(commands=['feedback'])
def info(message):
    global SwitchTracker
    SwitchTracker = 2
    bot.send_message(message.chat.id, "Пиши все, что думаешь об этом боте")
@bot.message_handler(commands=['game'])
def game(message):
    bot.send_message(message.chat.id, "Пиши какую игру хочешь скачать")
    global SwitchTracker
    SwitchTracker = 1
@bot.message_handler(content_types=["text"])
def msg(message):
    global SwitchTracker
    global mesg
    if SwitchTracker == 1:
        GetGamehtml(message.text.encode('utf-8').decode("utf-8"))
        mesg = message.text.encode('utf-8').decode("utf-8")
        if os.path.exists("/home/usr/Desktop/game.torrent"):
            bot.send_message(message.chat.id, "Вот, что нашел:")
            bot.send_message(message.chat.id, Name[0] + "\n💾Скачать: /1")
            try:
                bot.send_message(message.chat.id, Name[1] + "\n💾Скачать: /2")
            except IndexError:
                pass
            try:
                bot.send_message(message.chat.id, Name[2] + "\n💾Скачать: /3")
            except IndexError:
                pass
            bot.send_message(message.chat.id, "Какой качаем?")
            Name.clear()
            if Choise == 0:
                pass
            os.remove("/home/usr/Desktop/game.torrent")
        else:
            bot.send_message(message.chat.id, "Упс, торрента с таким именем нет на трекере ☹️")
    elif SwitchTracker == 0:
        GetHtml(message.text.encode('utf-8').decode("utf-8"))
        mesg = message.text.encode('utf-8').decode("utf-8")
        if os.path.exists("/home/usr/Desktop/torrent.torrent"):
            bot.send_message(message.chat.id, "Вот, что нашел:")
            bot.send_message(message.chat.id, Name[2] + "\n💾Скачать: /1")
            try:
                bot.send_message(message.chat.id, Name[5] + "\n💾Скачать: /2")
            except IndexError:
                pass
            try:
                bot.send_message(message.chat.id, Name[8] + "\n💾Скачать: /3")
            except IndexError:
                pass
            bot.send_message(message.chat.id, "Какой качаем?")
            Name.clear()
            if Choise == 0:
                pass
            os.remove("/home/usr/Desktop/torrent.torrent")
        else:
            bot.send_message(message.chat.id, "Упс, торрента с таким именем нет на трекере ☹️")
    elif SwitchTracker == 2:
        f = open('/home/usr/Desktop/feedback.txt', 'a')
        f.write(message.text + "\n")

def GetHtml(i):
    print(i)
    res = re.sub(r'\s','%20', i)
    url = "http://vip-tor.org/search/0/0/000/2/" + quote(res)
    print(res)
    resp = urllib.request.urlopen(url)
    Parser(resp.read())

def GetGamehtml(i):
    res = re.sub(r'\s', '+', i)
    url = "https://rg-mechanics.org/search/?q="+quote(res)+"&sfSbm=%D0%98%D1%81%D0%BA%D0%B0%D1%82%D1%8C"
    resp = urllib.request.urlopen(url)
    GameParser(resp.read())


def Parser(html):
    soup = BeautifulSoup(html, "lxml")
    tag = soup.find_all("tr", {'class': 'gai'})
    tag += soup.find_all("tr", {'class': 'tum'})
    hr = []
    name = ""
    global Name
    for i in tag:
        hr.append(i.find("a",{'class': 'downgif'}).get("href"))
        name += str(i.find_all('a'))
    soup1 = BeautifulSoup(str(name), "lxml")
    tag1 = soup1.find_all('a')
    for a in tag1:
        text = a.get_text()
        Name.append(text)
    try:
        print(Choise)
        Download(hr[0])
        if Choise == 1:
            Download(hr[0])
        elif Choise == 2:
            if len(hr)>1:
                Download(hr[1])
        else:
            if len(hr)>2:
                Download(hr[2])
    except:
        pass

def GameParser(html):
    soup = BeautifulSoup(html, "lxml")
    href = []
    link = []
    try:
        tag = soup.findAll("a", {'class': 'linkmater'})
        for i in tag:
            Name.append(i.get_text())
            href.append(i.get("href"))
        for n in href:
            resp = urllib.request.urlopen(n)
            soup2 = BeautifulSoup(resp.read(), "lxml")
            try:
                link.append(soup2.find("a", {'class': 'minibutton btn-download link12 block1 spoiler-trigger'}).get("href"))
            except Exception:
                link.append(soup2.find("a", {'class': 'minibutton btn-download link12 block1'}).get("href"))
        try:
            if Choise == 1:
                DownloadGame(link[0])
            elif Choise == 2:
                if len(link) > 1:
                    DownloadGame(link[1])
            else:
                if len(link) > 2:
                    DownloadGame(link[2])
        except:
            pass
    except:
        pass

def Download(href):
    urllib.request.urlretrieve("http://vip-tor.org" + href, '/home/usr/Desktop/torrent.torrent')

def DownloadGame(href):
    try:
        urllib.request.urlretrieve("https:"+ href,'/home/usr/Desktop/game.torrent')
    except Exception:
        urllib.request.urlretrieve("https://rg-mechanics.org" + href, '/home/usr/Desktop/game.torrent')

if __name__ == '__main__':
    bot.polling(none_stop=True)