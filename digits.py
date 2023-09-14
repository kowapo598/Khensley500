#============== IMPORTING SHIIII ===============#
import os, time, random, platform, colorama
from colorama import Fore, Back, Style
from datetime import datetime
import configparser
from random import randrange
from random import choice
from configparser import ConfigParser
import undetected_chromedriver as uc
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#============== DONE IMPORTING ===============#
#============== Moudles ===============#
colorama.init()
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
gr = Fore.GREEN
ble = Fore.BLUE
cy = Fore.CYAN
bwh = Back.WHITE
byl = Back.YELLOW
bred = Back.RED
bgr = Back.GREEN
#####################################################

def main():
     os.system('title SMS Sender ')
     os.system('cls' if platform.system() == 'Windows' else 'clear')
     read_config = configparser.ConfigParser()
     read_config.read("config.ini")
#===========================            ============================#
     print(Fore.GREEN+'****************************************************************************************************')
     print(Fore.GREEN+'                                                                          ')
     print(Fore.GREEN+'         ----🔥   PRIV8 BULK SMS S3NDER BY MILLER LICENSED TO XOXO 🔥----             ')
     print('                                                                                          ')
     print('                                                                                          ')
     print('--------------------------------------------------------------------------------------------------------')
     print('                                                                                          ')
     print('[+]  Loading up........                                            ')
     print('                                                                Para-Mode                          ')
#     options = uc.ChromeOptions()
#     options.headless=True
     browser = uc.Chrome();
     browser.maximize_window()
     browser.get("Put Your Digit Url")
     browser.implicitly_wait(8)
     wait = WebDriverWait(browser, 20)
     time.sleep(8)
     registerbtn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[4]/button')))
     registerbtn.click()
     time.sleep(3)
     print('[+] Logged in Successfully                                                                                         ')
     print('                                                                                          ')
     num = input("Input Leads file : ")
     print('                                                                                          ')
     time.sleep(4)
     with open(num) as NumList:
      argFile = NumList.read().splitlines()
      for data in argFile:
       try:
          addbutn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/span/div[2]/div/div/div[1]/div/div[1]/div[2]/div/a/div/button/div')))
          addbutn.click()
          time.sleep(4)
          numbtab = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/span/div[2]/div/div/div[2]/div[1]/div/div[1]/div[3]/div/input')))
          numbtab.send_keys(data);
          time.sleep(4)
          message  = read_config.get("Section1", "message")
          gen_rand = "RAND"
          number = random.randint(10000,99999)
          message = message.replace(gen_rand, str(number))
          messagebt = browser.find_element(By.CLASS_NAME, 'DraftEditor-editorContainer')
          messagebt.click()
          time.sleep(4)
          typed = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/span/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div')))
          typed.send_keys(message);
          time.sleep(4)
          typed.send_keys(Keys.ENTER);
          print(f'[+] Message sent successfully to '+ data +' ......');
          time.sleep(4)
       except:
          print(f'[+] Failure to send message to '+ data +' ......');
          f= open("failed.txt","w+")
          f.write(data)
          f.close()
          time.sleep(2)
       continue
#===========================            ============================#
if __name__ == '__main__':
    main()