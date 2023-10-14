#!/usr/bin/python3
import webbrowser
import time
import os


for i in range(10):
    pos = i
    url='https://webglsamples.org/aquarium/aquarium.html?numFish=5000'
    print(os.system(f"chromium-browser --new-window --window-size=800,600 --window-position={pos},{pos} {url} &"))

#time.sleep(60)
#os.system('pkill chromium')
#--window-position={pos},{pos} {url}
