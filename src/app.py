# Copyright (c) 2024 Halil İbrahim ÇAKIR
# Licensed under the MIT License. See LICENSE file for details.
import pyautogui
import time
from datetime import datetime  # Zaman bilgisini almak için

second = 1
second = int(input("Ne kadar sürede bir(varsayılan 1): "))

try:
    print("Program başlıyor. Çıkmak için Ctrl+C'ye basın.")
    while True:
        pyautogui.click()  # Fare tıklaması yapar
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Şu anki zamanı alır
        print(f"{current_time} Tıklandı!")
        time.sleep(second)  # Belirtilen sürede bekler
except KeyboardInterrupt:
    print("Program durduruldu.")
