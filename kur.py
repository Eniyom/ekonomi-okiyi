from bs4 import BeautifulSoup
from pygame import mixer 
import requests
import time

mixer.init() 
max = float(0)
min = float(0)
prv = float(0)
runtime = 0
crt = False
past = None
while True:
    try:
        r = requests.get('http://bigpara.hurriyet.com.tr/doviz/dolar/')
        past = r
    except:
        print("Bir Hata Meydana Geldi Önceki Veri Kullanılıyor....")
        r = past
    src = BeautifulSoup(r.content,"lxml")
    rate = src.find("div",attrs={"class":"kurDetail mBot20"}).findChildren('div')[2].findChildren('span')[1].text
    rate = float(rate.replace(',','.'))
    if min == 0:
        min = rate
    if rate > max:
        mixer.music.load("pik.mp3")
        mixer.music.play()
        max = rate
        crt = True
    if rate < min:
        mixer.music.load("mehter.mp3")
        mixer.music.play()
        min = rate
        crt = True
    print(f"Şimdiki kur: {rate}, Max: {max}, Min: {min}, Program {runtime} saniyedir çalışıyor.")
    

    if runtime % 600 == 0 and crt == False:
        if prev > rate:
            mixer.music.load("mehter.mp3")
            mixer.music.play()
        elif prev < rate: 
            mixer.music.load("pik.mp3")
            mixer.music.play()
        print(f"10 Dakikalık Uyarı: {prev} > {rate} ")
        min = 0
        max = 0
    prev = rate
    runtime = runtime+10
    time.sleep(10)
    crt = False
    