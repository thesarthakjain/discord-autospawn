import time
from selenium import webdriver
import cred
from cryptography.fernet import Fernet



message = "I am a robot"                                                                #text for the gif
site_link = "https://discord.com/channels/733191579162116116/748197273632243762"        #link of the specific discord channel
mins = 10                                                                               #number of minutes you want the autospawn to work



def spawner():
    gif_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[2]/div[1]')
    gif_button.click()
    print("GIF button pressed")

    time.sleep(2)

    message_box = driver.find_element_by_xpath('//*[@id="gif-picker-tab-panel"]/div[1]/div/div/div/input')
    message_box.send_keys(message)
    print("Text entered")

    time.sleep(6)

    send_button = driver.find_element_by_xpath('//*[@id="gif-picker-tab-panel"]/div[2]/div[1]/div/div/div[1]/video')
    send_button.click()
    print("Send button pressed")

    time.sleep(2)



def perform_login():
    email_box = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
    email_box.send_keys(email)
    print("Email ID entered")

    password_box = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
    password_box.send_keys(password)
    print("Password entered")

    login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
    login_button.click()
    print("Send button pressed")


file = open('key.key', 'rb')
key = file.read()
file.close()
f = Fernet(key)
email = f.decrypt(cred.email.encode()).decode()
password = f.decrypt(cred.password.encode()).decode()

driver = webdriver.Chrome('D:\Desktop\PythonProj\chromedriver')
print("Opening",site_link)
driver.get(site_link)
print("Site opened")

time.sleep(5)

perform_login()

time.sleep(5)

for i in range(mins):
    spawner()
    time.sleep(50)

time.sleep(60)
print("Site closed")
driver.close()