
#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time
#file wo file h jisme hmara usic h aur stopper music ko stop krega
def musiconloop(file, stopper):
    mixer.init() #init 1 function h init ke andar
    mixer.music.load(file) #loading a music file
    mixer.music.play()
    while True: #file ko load hone ke liye tym dena hoga isiliye while true lgega
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
#----------------------login function----------------------------
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
     #musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

while True:
    if time() - init_water > watersecs:
        print("Water Drinking time. Enter 'drank' to stop the alarm.")
        musiconloop('water.mp3', 'drank')
        init_water = time() #again reinitialize water
        log_now("Drank Water at")

    if time() - init_eyes >eyessecs:
        print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
        musiconloop('eyes.mp3', 'doneeyes')
        init_eyes = time()
        log_now("Eyes Relaxed at")

    if time() - init_exercise > exsecs:
        print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
        musiconloop('physical.mp3', 'donephy')
        init_exercise = time()
        log_now("Physical Activity done at")