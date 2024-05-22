import os
import sys
import socket
import time
import hashlib
from playsound import playsound
import winsound
import colorama
from colorama import Fore, Style

if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
# .exe dosyasının çalışma dizinini bulunduğu klasör olarak belirliyor
cwd = os.getcwd()
# print(cwd) (Çalışma Dizini Kontrolü)
hostname = socket.gethostname()
# Bilgisayardaki kullanıcı adını okur
colorama.init(autoreset=True)
# Yazı Stillerini Birbirinden Ayrı Tutuyor


def urun_ekle():
    print(f"{Fore.RESET}Bu Seçenekte Ürün Ekleme Yeri Çıkıcak")


def urun_bilgi():
    print(f"{Fore.RESET}Bu Seçenekte Ürün Bilgi Yeri Çıkıcak")


def urun_sil():
    print(f"{Fore.RESET}Bu Seçenekte Ürün Silme Yeri Çıkıcak")


def urun_transfer():
    print(f"{Fore.RESET}Bu Seçenekte Ürün Transfer Yeri Çıkıcak")

def yeni_sifre_olustur():
    while True:
        yeni_sifre = input(f"{Fore.LIGHTWHITE_EX}Yeni Şifrenizi Belirleyin:{Fore.RESET} ")
        if not yeni_sifre:
            print(f"{Fore.LIGHTRED_EX}Şifre Giriş Alanı Boş Bırakılamaz!\n")
            playsound(f"{cwd}//assests//error_sound.wav", block=False)
            continue
        else:
            yeni_sifre_tekrar = input(f"{Fore.LIGHTWHITE_EX}\nYeni Şifrenizi Tekrar Girin:{Fore.RESET} ")
            if yeni_sifre == yeni_sifre_tekrar:
                hashlenmis_yeni_sifre = hashlib.sha512(yeni_sifre.encode('utf-8')).hexdigest()
                with open('password_file.txt', 'w') as file:
                    file.write(hashlenmis_yeni_sifre)
                    pass_file_dir = f"{cwd}//password_file.txt"
                    os.chmod(pass_file_dir, 0o444)
                    os.system(f" attrib +h {cwd}//password_file.txt")
                    # "attrib +h" ibaresi kaydedilen dosyayı gizli yapar. "-h" ile dosyayı görünür yapabilirsin
                    # Dosyayı görmek için "seçenekler -> görünüm -> Gizli dosya, klasör veya sürücüleri göster" seçeneğini seçin
                    # (41) 0o ibaresi yazılan sayının 8'lik tabanda yazılacağını gösterir.
                print(f"{Fore.LIGHTGREEN_EX}Yeni Şifre Başarıyla Oluşturuldu. Giriş Yapılıyor...")
                playsound(f"{cwd}//assests//logon_sound.wav", block=False)
                time.sleep(1)
                break
            else:
                print(f"{Fore.LIGHTRED_EX}Girdiğiniz Şifreler Uyuşmuyor. Tekrar Deneyin.\n")
                playsound(f"{cwd}//assests//error_sound.wav", block=False)
                continue

try:
    while True:
        with open((f'{cwd}//password_file.txt'), 'r') as file:
            hashlenmis_dogru_sifre = file.read()
            sifre_giris = (input(f"{Fore.LIGHTWHITE_EX}Lütfen Şifrenizi Giriniz{Fore.RESET}\n"))
            hashlenmis_sifre_giris = hashlib.sha512(sifre_giris.encode('utf-8')).hexdigest()
            # (55) Girilen şifreyi sha512 algoritmasıyla hashler hexdigest kullanılmasının sebebi çok uzun olan binary hashını 16'lık tabanda yazmaktır
        if hashlenmis_dogru_sifre == hashlenmis_sifre_giris:
            print(f"{Fore.LIGHTGREEN_EX}Şifreniz Doğru. Giriş Yapılıyor...")
            playsound(f"{cwd}//assests//logon_sound.wav", block=False)
            time.sleep(1)
            break
        elif not sifre_giris:
            print(f"{Fore.LIGHTRED_EX}Şifre Giriş Alanı Boş Bırakılamaz!\n")
            playsound(f"{cwd}//assests//error_sound.wav", block=False)
            continue
        else:
            print(f"{Fore.LIGHTRED_EX}Şifreniz Yanlış! Tekrar Deneyiniz.\n")
            playsound(f"{cwd}//assests//error_sound.wav", block=False)
            continue
except FileNotFoundError as hata:
    print(f"{Fore.LIGHTRED_EX}Şifre Dosyası Bulunmuyor. Yeni Şifre Oluşturun\n")
    playsound(f"{cwd}//assests//error_sound.wav", block=False)
    yeni_sifre_olustur()

print(f"""{Fore.LIGHTCYAN_EX}{Style.BRIGHT}
    ____                      ______      __   _          _____ _      __                 _ 
   / __ \\___  ____  ____     /_  __/___ _/ /__(_)___     / ___/(_)____/ /____  ____ ___  (_)
  / / / / _ \\/ __ \\/ __ \\     / / / __ `/ //_/ / __ \\    \\__ \\/ / ___/ __/ _ \\/ __ `__ \\/ / 
 / /_/ /  __/ /_/ / /_/ /    / / / /_/ / ,< / / /_/ /   ___/ / /\\_  / /_/  __/ / / / / / /  
/_____/\\___/ .___/\\____/    /_/  \\____/_/|_/_/ .___/   /____/_/____/\\__/\\___/_/ /_/ /_/_/   
          /_/                               /_/   
{Style.BRIGHT}{Fore.WHITE}
Uygulamasına Hoş Geldin {hostname}!
""")
while True:
    print(f"""
{Fore.LIGHTWHITE_EX}Lütfen Yapmak İstediğiniz İşlemi Seçiniz:
{Fore.CYAN}1 {Fore.RESET}- Ürün Ekle
{Fore.CYAN}2 {Fore.RESET}- Ürün Bilgilerini Göster
{Fore.CYAN}3 {Fore.RESET}- Ürün Sil
{Fore.CYAN}4 {Fore.RESET}- Ürün Transfer Et
{Fore.LIGHTMAGENTA_EX}5 {Fore.RESET}- Arka Plan Müziğini Oynat
{Fore.LIGHTMAGENTA_EX}6 {Fore.RESET}- Arka Plan Müziğini Durdur
    """)
    try:
        secim = int(input(f"{Fore.CYAN}"))
        if secim == 1:
            urun_ekle()
        elif secim == 2:
            urun_bilgi()
        elif secim == 3:
            urun_sil()
        elif secim == 4:
            urun_transfer()
        elif secim == 5:
            print(f"""{Fore.LIGHTWHITE_EX}
Lütfen İstediğiniz Şarkıyı Seçiniz:
{Fore.CYAN}1{Fore.RESET} - Night Vibes
{Fore.CYAN}2{Fore.RESET} - Lofi Music
            """)
            try:
                muzik_secim = int(input(f"{Fore.CYAN}"))
                if muzik_secim == 1:
                    winsound.PlaySound(f"{cwd}//assests//background_music1.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
                    # winsound.SND_LOOP sesi döngüye almayı sağlar. winsound.SND_ASYNC ise şarkı çalmaya devam ederken diğer kodları çalıştırmaya devam eder
                elif muzik_secim == 2:
                    winsound.PlaySound(f"{cwd}//assests//background_music2.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
                else:
                    print(f"\n{Fore.LIGHTRED_EX}Lütfen Geçerli Bir Sayı Giriniz! (1-2)")
                    playsound(f"{cwd}//assests//error_sound.wav", block=False)
            except ValueError:
                print(f"\n{Fore.LIGHTRED_EX}Lütfen Bir Sayı Giriniz!")
                playsound(f"{cwd}//assests//error_sound.wav", block=False)
        elif secim == 6:
            winsound.PlaySound(None, winsound.SND_PURGE)
            # winsound.SND_PURGE çalan sesleri kapatır
        else:
            print(f"\n{Fore.LIGHTRED_EX}Lütfen Geçerli Bir Sayı Giriniz! (1-4)")
            playsound(f"{cwd}//assests//error_sound.wav", block=False)
            # 'block=False' ifadesi sesin bitmesini beklemeden kodun çalışmasına devam etmesini sağlıyor
    except ValueError:
        print(f"\n{Fore.LIGHTRED_EX}Lütfen Bir Sayı Giriniz!")
        playsound(f"{cwd}//assests//error_sound.wav", block=False)
