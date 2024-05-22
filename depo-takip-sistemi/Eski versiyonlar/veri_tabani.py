"""
Python Version: 3.12
File: veri_tabani.py
Created Date: 2024-03-27
Author: Cemil İlkim Teke
Pylint Score: 8.22/10
Description: A module for depo_takip_sistemi.py file that takes care of with sqlite3 connection and manipulation
"""
import hashlib
import sqlite3 as sql
import os
import sys
import colorama
from colorama import Fore, Style
from playsound import playsound
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import random
# Exe dosyasında "veri_tabani.db" dosyasını gizli oluşturmaya yarar.
import subprocess

if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
# .exe dosyasının çalışma dizinini bulunduğu klasör olarak belirliyor
cwd = os.getcwd()


def tablo_olustur():
    conn = sql.connect('veri_tabani.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS USERS(
    Username TEXT,
    Password TEXT,
    Mail TEXT
    )""")
    conn.commit()
    conn.close()
    cwd = os.getcwd()
    db_path = os.path.join(cwd, 'veri_tabani.db')
    subprocess.run(['attrib', '+h', db_path], shell=True)


def dogrulama_maili_gonder(username):
    conn = sql.connect(f'{cwd}//veri_tabani.db')
    c = conn.cursor()
    kullanici_kontrol = """SELECT COUNT(*) FROM USERS WHERE username = ?"""
    c.execute(kullanici_kontrol, (username,))
    if c.fetchone()[0] == 0:
        print(f"{Fore.LIGHTRED_EX}Kullanıcı bulunamadı!\n")
        conn.close()
        return None
    mail_al = """SELECT mail FROM USERS WHERE Username= ?"""
    data = (username,)
    c.execute(mail_al, data)
    mail = c.fetchone()[0]
    print(mail)
    conn.close()
    subject = "Depo Takip Sistemi"
    kod = random.randint(100000, 999999)
    # Gönderilen mailin daha güzel gözükmesi için html ve css kodu kullandım
    body = f"""
<html>
<head>
    <title>Depo Takip Sistemi</title>
</head>
<body style="background-color: #b3b3b3; color: white; font-family: Arial, sans-serif; text-align: center; margin: 0;">
<table cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #b3b3b3;">
    <tr>
        <td style="padding: 40px;">
            <table cellspacing="0" cellpadding="0" border="0" align="center" width="300" style="background-color: white; border-top-right-radius: 35px; border-top-left-radius: 35px; box-shadow: 0 4px 8px rgba(0,0,0,0.7);">
                <tr>
                    <td>
                        <h1 style="color: black; text-align: center;">Depo Takip Sistemi</h1>
                    </td>
                </tr>
            </table>
            <table cellspacing="0" cellpadding="0" border="0" align="center" width="300" style="background-color: black; color: white; padding: 10px; border-bottom-right-radius: 35px; border-bottom-left-radius: 35px; box-shadow: 0 4px 8px rgba(0,0,0,0.7);">
                <tr>
                    <td style="padding: 0;">
                        <p style="font-size: 15px; color:white;">Doğrulama Kodunuz:</p>
                        <div style="background-color: white; color: black; padding: 5px; border-radius: 5px; margin-top: 10px; font-size: 25px; text-align: center;"><strong>{kod}</strong></div>
                        <p style="color: white; font-size: 15px">Lütfen Bu Maile Cevap Vermeyiniz!</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
</body>
</html>
"""
    # Mail bağlantısı oluşturma
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    gonderen_mail = "depotakipsistemi@gmail.com"
    server.login(gonderen_mail, "zqbkgmzlhhfuuowu")
    # Mail'i oluşturur
    msg = MIMEMultipart()
    msg['From'] = gonderen_mail
    msg['To'] = mail
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    # Mesaj içeriğini belirtiyoruz
    # E-postayı gönderir
    server.sendmail(gonderen_mail, mail, msg.as_string())
    print(f"\n{Fore.LIGHTGREEN_EX}Mail Başarıyla Gönderildi")
    # Bağlantıyı kapatır
    server.quit()
    dogrulama_kodu = int(input("\nLütfen Mailinize Gelen Doğrulama Kodunu Giriniz:\n"))
    dogrulama_maili(username, kod, dogrulama_kodu)


def dogrulama_maili(username, kod, dogrulama_kodu):
    if int(dogrulama_kodu) == kod:
        while True:
            new_pass = str(input("\nLütfen Yeni Şifrenizi Giriniz:\n"))
            new_pass = hashlib.sha512(new_pass.encode()).hexdigest()
            new_pass_again = str(input("\nLütfen Yeni Şifrenizi Tekrar Giriniz:\n"))
            new_pass_again = hashlib.sha512(new_pass_again.encode()).hexdigest()
            if new_pass == new_pass_again:
                sifre_degistir(username, new_pass)
                break
            else:
                print(f"\n{Fore.LIGHTRED_EX}Şifreleriniz Uyuşmuyor!")
                playsound(f"{cwd}//assests//error_sound.wav", block=False)
                continue
    else:
        print(f"\n{Fore.LIGHTRED_EX}Girdiğiniz Doğrulama Kodu Eşleşmiyor!\n")
        playsound(f"{cwd}//assests//error_sound.wav", block=False)


def sifre_degistir(username, new_pass):
    conn = sql.connect(f'{cwd}//veri_tabani.db')
    c = conn.cursor()
    sifre_degistir = """UPDATE USERS SET password = ? WHERE username = ?"""
    data = (new_pass, username)
    c.execute(sifre_degistir, data)
    conn.commit()
    print(f"\n{Fore.LIGHTGREEN_EX}Şifreniz Başarıyla Değiştirildi!\n")
    conn.close()


def hizli_erisim_ekle(mail):
    conn = sql.connect('veri_tabani.db')
    c = conn.cursor()
    # Create the table if it doesn't exist
    c.execute("""CREATE TABLE IF NOT EXISTS FAST_ACCESS
                 (mail TEXT)""")
    ekle = 'INSERT INTO FAST_ACCESS (mail) VALUES (?)'
    kontrol = """SELECT COUNT(*) FROM FAST_ACCESS WHERE mail = ?"""
    c.execute(kontrol, (mail,))
    if c.fetchone()[0] > 0:
        print(f"{Fore.LIGHTRED_EX}Bu Mail Adresi Zaten Kayıtlı.")
        playsound(f"{cwd}//assests//error_sound.wav", block=False)
        conn.close()
        return
    data = (mail,)
    c.execute(ekle, data)
    conn.commit()
    print(f"{Fore.LIGHTGREEN_EX}Hızlı Erişim Başarıyla Eklendi.")
    conn.close()


def hizli_erisim_goster():
    conn = sql.connect('veri_tabani.db')
    c = conn.cursor()
    try:
        c.execute('SELECT rowid, mail FROM FAST_ACCESS')
    except sql.OperationalError:
        print(f"\n{Fore.LIGHTRED_EX}Hızlı Erişimler Tablosu Bulunmuyor!")
        playsound(f"{cwd}//assests//error_sound.wav", block=False)
        conn.close()
        return None
    mails = c.fetchall()
    conn.close()
    print("Hızlı Erişim Mailleri:")
    for mail in mails:
        print(f"ID: {mail[0]}, Mail: {mail[1]}")


def hizli_erisim_sec():
    conn = sql.connect('veri_tabani.db')
    c = conn.cursor()
    rowid = int(input("\nGöndermek İstediğiniz Mailin ID'sini Giriniz.\n\n"))
    c.execute('SELECT mail FROM FAST_ACCESS WHERE rowid=?', (rowid,))
    selected_mail = c.fetchone()
    conn.close()
    if selected_mail:
        print(f"\nSeçilen Mail: {selected_mail[0]}\n")
        mail = selected_mail[0]
        return mail
    else:
        print(f"\n{Fore.LIGHTRED_EX}Geçersiz Sıra.\n")
        playsound(f"{cwd}//assests//error_sound.wav", block=False)
        return None


def kullanici_ekle(username, mail, password):
    if not password:  # Şifre alanı boşsa
        print(f"{Fore.LIGHTRED_EX}Şifre Alanı Boş Bırakılamaz.\n")
        playsound(f"{cwd}//assests//error_sound.wav", block=False)
        return
    conn = sql.connect(f'{cwd}//veri_tabani.db')
    c = conn.cursor()
    # Kullanıcı adı kontrolü
    kontrol = """SELECT COUNT(*) FROM USERS WHERE username = ?"""
    c.execute(kontrol, (username,))
    if c.fetchone()[0] > 0:
        print(f"{Fore.LIGHTRED_EX}Bu Kullanıcı Adı Zaten Kullanılıyor.\n")
        playsound(f"{cwd}//assests//error_sound.wav", block=False)
        conn.close()
        return
    ekle = """INSERT INTO USERS (username, mail, password) VALUES (?,?,?)"""
    data = (username, mail, password)
    c.execute(ekle, data)
    conn.commit()
    print(f"\n{Fore.LIGHTGREEN_EX}Kayıt Olundu.\n")
    conn.close()


def kullanici_sil(username, password):
    conn = sql.connect(f'{cwd}//veri_tabani.db')
    c = conn.cursor()
    sil = """DELETE FROM USERS WHERE username = ? AND password = ?"""
    data = (username, password)
    c.execute(sil, data)
    conn.commit()
    conn.close()
    if username != "admin":
        if c.rowcount > 0:  # Etkilenen satır sayısına bakarak silme işleminin başarılı olup olmadığını kontrol et
            print(f"{Fore.LIGHTGREEN_EX}\nKullanıcı Silindi.")
            return True
        else:
            print(f"{Fore.LIGHTRED_EX}\nKullanıcı Adı Veya Şifre Hatalı.")
            playsound(f"{cwd}//assests//error_sound.wav", block=False)
            return False
    else:
        print(f"{Fore.LIGHTRED_EX}Admin Kullanıcı Silinemez")
        playsound(f"{cwd}//assests//error_sound.wav", block=False)


def kullanici_ara(username):
    conn = sql.connect(f'{cwd}//veri_tabani.db')
    c = conn.cursor()
    ara = """SELECT username, mail FROM USERS WHERE username = ?"""
    data = (username,)
    c.execute(ara, data)
    user_list = c.fetchall()
    conn.close()
    if user_list:
        return user_list
    else:
        return None


def sifre_giris(username, password):
    if not password:  # Şifre alanı boşsa
        print(f"{Fore.LIGHTRED_EX}Şifre Alanı Boş Bırakılamaz.")
        playsound(f"{cwd}//assests//error_sound.wav", block=False)
        return False
    conn = sql.connect(f'{cwd}//veri_tabani.db')
    c = conn.cursor()
    giris = """SELECT Username FROM USERS WHERE Username = ? AND Password = ?"""
    data = (username, password)
    c.execute(giris, data)
    result = c.fetchone()  # Kullanıcı adı ve şifreye karşılık gelen bir sonuç al
    conn.close()
    return result is not None  # Sonuç varsa True, yoksa False döndür


tablo_olustur()
