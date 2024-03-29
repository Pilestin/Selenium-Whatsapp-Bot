from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from info import target, message, auto_send
import time 
import ctypes  


def intro():
    """ Uygulama başlatıldığında bizi karşılayan tanıtım mesajları """

    print("\n\n---------------------- Selenium Whatsapp Bot / Yasin Ünal----------------------\n\n")
    time.sleep(1)
    print("  Bu script belirtilen kişi veya gruba mesaj gönderir.")
    time.sleep(1)
    print("  WP karekodunu okutup, whatsapp içeriğini gördükten sonra tekrar buraya gelip göndermek istediğin mesajı gir ")
    time.sleep(3)
    ctypes.windll.user32.MessageBoxW(0, "chromedriver.exe dosyasının webdriver/chromedriver.exe dizininde bulunduğundan eminsen tamama tıkla", "Dikkat", 0)

def menu():
    # ! Burası şu an kullanılmıyor. Direk info.py içerisinden emir alınıyor.
    """ Kullanıcıdan seçimin alındığı menu görevi gören metod"""

    print("")
    print("|--------------------| MENU |---------------------|") 
    print("| 1-Kişiye mesaj yaz ama göndermeyi ben yapacağım |")
    print("| 2-Kişiye mesaj yaz ve gönder                    |")
    print("| 3-Çıkış                                         |")
    print("|-------------------------------------------------|") 
    op = input("|Seçiminiz : ")
    print("")
    return op

def getName():
    """ Mesaj kime gönderilecek bilgisini alıp , döndürür. """

    # target    = input("Mesajını kime göndereceksin( İsmi doğru girmelisin) : ")
    return target

def getMessage():
    """ Mesaj bilgisini alır , döndürür. """

    # message = input("Mesajını girebilirsin (Mesajı girdikten sonra ENTER'a tıklamalısın) : ")
    return message

def setAction(driver , auto_send_message = False):

    target      = getName()       # kime mesaj atılacak
    mymessage   = getMessage()   # ne mesajı atılacak
    time.sleep(1)
    # whatsapp'da görülen arama kutucuğunun yeri
    nameSearchBox = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]")
    time.sleep(1)
    nameSearchBox.send_keys(target)
    time.sleep(1)
    nameSearchBox.send_keys(Keys.ARROW_DOWN) # Gelen sonuclardan en üsttekinin doğru oldupu varsayılır.( Bir alta inilir)
    # choosenBox    = driver.find_elements(By.CLASS_NAME, "_3OvU8")
    time.sleep(1)
    massageBox = driver.find_element(By.XPATH , "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    time.sleep(1)
    massageBox.send_keys(mymessage)
    if(auto_send_message): 
        massageBox.send_keys(Keys.ENTER)
    time.sleep(1) 

def out():
    print("\n\n|----------------------------------|")
    input("|Denediğin için teşekkürler|")
    print("|----------------------------------|\n\n")

def WP():
    """ Tüm işlemlerin yönetildiği ve tutulduğu panel-metod"""

    intro()
    driver = webdriver.Chrome(executable_path = "webdriver/chromedriver.exe" ) # Buraya kendi webdriver path'inizi verin.
    driver.get("https://web.whatsapp.com/")  #  url'yi verelim
    time.sleep(4)
    print(" ! Whatsapp'a giriş yapmadan mesaj girme")

    ctypes.windll.user32.MessageBoxW(0, "QR kodu okuttuysan devam etmek için tamama tıkla", "Dikkat", 0)

    while(True):
        # info.py içerisinden alınan bilgi setAction metoduna gönderilir.
        setAction(driver , auto_send_message=auto_send)
        break

    out()
    driver.close()

WP()
