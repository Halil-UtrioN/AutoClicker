# Copyright (c) 2024 Halil İbrahim ÇAKIR
# Licensed under the MIT License. See LICENSE file for details.
import pyautogui
import time
from datetime import datetime  # Zaman bilgisini almak için
import logging # Hata mesajlarını kaydetmek için
import os # Dosya işlemleri için

#AutoClick.log dosyasını oluşturmak için konum belirliyoruz.
userDir = os.path.expanduser('~') #Kullanıcı klasörünü buluyoruz.
appDir = os.path.join(userDir, 'AutoClick') #Log dosyasını oluşturacağımız klasörü belirliyoruz.
# Klasör yoksa oluştur
if not os.path.exists(appDir):
    os.makedirs(appDir)

log_path = os.path.join(appDir, "AutoClick.log") # Log dosyasının tam yolu

# Logging yapılandırması
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info("Uygulama Başlatıldı")

second = 1
while True:
    try:
        second = int(input("Saniye cinsinden tam sayı giriniz (varsayılan 1): "))
        logging.info(f"Değer verildi. Değer = {second}")
        break #Doğru şekilde değer verilirse
    except ValueError:
        logging.warning("Varsayılan değer atandı")
        print("Varsayılan değer atandı.")
        break # Değer verilemdi, varsayılan değer 1

try:
    logging.info("Döngü başlatıldı")
    print("Program başlıyor. Çıkmak için Ctrl+C'ye basın.")
    while True:
        pyautogui.click()  # Fare tıklaması yapar
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Şu anki zamanı alır
        print(f"{current_time} Tıklandı!")
        logging.info("Tıklama gerçekleşti")
        time.sleep(second)  # Belirtilen sürede bekler
except KeyboardInterrupt:
    logging.info("Program sonlandırıldı")
    print("Program durduruldu.")