from settings import TimeSettings
from util import about
from util import to_pickle
from util import read_pickle

import bs4 as bs
import pandas as pd
import numpy as np
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
from keyboard import press
from datetime import datetime

t = TimeSettings()

def open_whatsapp(phone, headless=False):
    url = 'https://api.whatsapp.com/send?phone=' + phone + '&text='
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(t.load_pg)

    chains = ActionChains(driver)
    hover = chains.move_to_element(driver.find_element_by_id("action-button"))
    hover.click().perform()
    
    print('Connected to Whatsapp, please insert QR code.')
    time.sleep(t.load_qr)
    return driver


def create_messages(msg_list, adlink, emojis):
    msg = random.choice(msg_list)
    emoji = random.choice(emojis)
    msg = msg + ' ' + emoji
    messages = [msg, adlink]
    return messages

def send_messages(driver, phones, msg_list, adlink):
    real_phones = []
    fake_phones = []
    for phone in phones:
        if datetime.now().hour < t.start_time: continue
        if datetime.now().hour > t.stop_time: continue

        try:
            messages = create_messages(msg_list, adlink)
            url = 'https://api.whatsapp.com/send?phone=' + phone + '&text='
            driver.get(url)
            time.sleep(t.load_pg)
            press('enter')
            press('enter')
            press('enter')
            time.sleep(t.load_pg)

            chains = ActionChains(driver)
            hover = chains.move_to_element(driver.find_element_by_id("action-button"))
            hover.click().perform()
            hover.click().perform()
            hover.click().perform()
            time.sleep(t.load_pg)

            chains = ActionChains(driver)
            hover = chains.move_to_element(driver.find_element_by_class_name("_1Plpp"))
            hover.click().perform()
            hover.reset_actions()

            for msg in messages:
                hover.send_keys(msg).perform()
                time.sleep(t.load_pg)
                hover.reset_actions()

                hover.send_keys(Keys.ENTER).perform()
                time.sleep(t.next_message)

            time.sleep(next_contact)
            real_phones.append(phone)
            to_pickle(real_phones, 'data/real_phones')
            
        except: 
            print('Could not send message.')
            fake_phones.append(phone)
            to_pickle(fake_phones, 'data/fake_phones')