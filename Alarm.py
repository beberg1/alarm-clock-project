# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:08:53 2019

@author: magnu
"""
from pygame import mixer 
import schedule
import time

mixer.init()
mixer.music.load('E:\Python prosjekt\Morgen\sang.mp3')


def job():
    print("God morgen")
    mixer.music.play()
    time.sleep(10)
    mixer.music.stop()
    return

schedule.every().day.at("15:28").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute
    





