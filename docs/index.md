# **SANAL ORTAMA GİRİŞ YAPMA**
- **_venv_** olarak terminali başlat:
    * `python -m venv venv` komutu ile yeni bir tane oluştur.
    * Eğer zaten varsa:
        * `source venv/bin/activate` (Linux/Mac)
        * `venv\Scripts\activate` (Windows)
        * Eğer Windwos tarafında sorun yaşıyorsan tek seferlik ByPass komutunu kullan ve tekrar aktif et.
        > ByPass etme komutu
        ```bash
        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        ```
- Çıkış yapabilmek için ise:
    * `deactivate` komutunu kullan.

# **Python Kütüpahanesi Kurulumu**
- Öncelikle terminali açıp venv aktivasyonu yap.
- Eğer ilk defa projeyi kurduysan gerekli kütüphaneleri kur:
    ```bash
    pip install -r requirements.txt
    ```
- `pip install kütüphane_ismi` komutu ile istediğin kütüpahaneleri kurabilirsin.
    * **Örnek:** `pip install flask`
- Eklediğin kütüpahaneyi `requirements.txt` dosyasına ekleyelim:
    ```bash
    pip freeze > requirements.txt
    ```
