from __future__ import unicode_literals
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
markup.row( '/game')
SwitchTracker = 0
# proxies = {
#   'http': '177.141.157.4',
#   'https': '177.141.157.4',
# }
#
# requests.get('tfile.co', proxies=proxies)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здаров, хочешь качнуть игруху? пиши /game в чат(эта хуйня не работает)! Если нет, то просто пиши название фильма или файла, все замутим",reply_markup=markup)
@bot.message_handler(commands=['game'])
def game(message):
    bot.send_message(message.chat.id, "Пиши какую игру хочешь скачать")
    global SwitchTracker
    SwitchTracker = 1
@bot.message_handler(content_types=["text"])
def msg(message):
    global SwitchTracker
    if SwitchTracker == 1:
        GetGamehtml(message.text.encode('utf-8').decode("utf-8"))
        if os.path.exists("/home/usr/Desktop/game.torrent"):
            bot.send_message(message.chat.id, "Окей, лови торрент")
            bot.send_document(message.chat.id,open('/home/usr/Desktop/game.torrent', 'rb'))
            os.remove("/home/usr/Desktop/game.torrent")
        else:
            bot.send_message(message.chat.id, "Упс, торрента с таким именем нет на трекере :(")
    elif SwitchTracker == 0:
        GetHtml(message.text.encode('utf-8').decode("utf-8"))
        if os.path.exists("/home/usr/Desktop/test1.torrent"):
            bot.send_message(message.chat.id, "Окей, лови торрент")
            bot.send_document(message.chat.id,open('/home/usr/Desktop/test1.torrent', 'rb'))
            os.remove("/home/usr/Desktop/test1.torrent")
        else:
            bot.send_message(message.chat.id, "Упс, торрента с таким именем нет на трекере :(")

def GetHtml(i):
    res = re.sub(r'\s','%20', i)
    url = "http://vip-tor.org/search/0/0/000/2/" + quote(res)
    print(res)
    resp = urllib.request.urlopen(url)
    Parser(resp.read())

def GetGamehtml(i):
    res = re.sub(r'\s', '+', i)
    url = "https://rg-mechanics.org/search/?q="+quote(res)+"&sfSbm=%D0%98%D1%81%D0%BA%D0%B0%D1%82%D1%8C"
    print(res)
    resp = urllib.request.urlopen(url)
    GameParser(resp.read())


def Parser(html):
    soup = BeautifulSoup(html, "lxml")
    tag = soup.find_all("tr", {'class': 'gai'})
    hr = []
    for i in tag:
        hr.append(i.find("a",{'class': 'downgif'}).get("href"))
    try:
        Download(hr[0])
    except:
        pass

def GameParser(html):
    soup = BeautifulSoup(html, "lxml")
    try:
        tag = soup.find("a", {'class': 'linkmater'}).get("href")
        resp = urllib.request.urlopen(tag)
        soup2 = BeautifulSoup(resp.read(), "lxml")
        try:
            link = soup2.find("a", {'class': 'minibutton btn-download link12 block1 spoiler-trigger'}).get("href")
        except Exception:
            link = soup2.find("a", {'class': 'minibutton btn-download link12 block1'}).get("href")
        print(link)
        DownloadGame(link)

    except Exception:
        print(Exception)

def Download(href):
    urllib.request.urlretrieve("http://vip-tor.org" + href, '/home/usr/Desktop/test1.torrent')

def DownloadGame(href):
    try:
        urllib.request.urlretrieve("https:"+ href,'/home/usr/Desktop/game.torrent')
    except Exception:
        urllib.request.urlretrieve("https://rg-mechanics.org" + href, '/home/usr/Desktop/game.torrent')

if __name__ == '__main__':
    bot.polling(none_stop=True)