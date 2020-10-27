from bs4 import BeautifulSoup
from pygame import mixer 
import requests
import time

mixer.init() 
max = float(0)
min = float(0)
runtime = 0
while True:
    r = requests.get('http://bigpara.hurriyet.com.tr/doviz/dolar/')

    src = BeautifulSoup(r.content,"lxml")
    rate = src.find("div",attrs={"class":"kurDetail mBot20"}).findChildren('div')[2].findChildren('span')[1].text
    rate = float(rate.replace(',','.'))
    if min == 0:
        min = rate
    if rate > max:
        mixer.music.load("pik.mp3")
        mixer.music.play()
        max = rate
    if rate < min:
        mixer.music.load("mehter.mp3")
        mixer.music.play()
        min = rate
    print(f"Şimdiki kur: {rate}, Max: {max}, Min: {min}, Program {runtime} saniyedir çalışıyor.")
    time.sleep(5)
    runtime = runtime+5