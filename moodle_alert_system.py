import requests
from bs4 import BeautifulSoup

def get_div_class(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")
    element = bs.find_all('div', class_="post-content-container")[:3]
    notice_list = []

    for notice in element:
        notice_list.append(notice.text)
    return notice_list

def get_h3_class(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")
    element = bs.find_all('h3', class_="h6 font-weight-bold mb-0")[:3]
    title_list = []

    for title in element:
        title_list.append(title.text)
    return title_list

def get_time_element(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")
    element = bs.find_all("time")[:3]
    time_list = []

    for time in element:
        time_list.append(time.text)
    return time_list


def telegram_notification(send):
   bot_token = "YOUR BOT TOKEN"
   my_chatID = "YOUR CHAT ID"
   send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + my_chatID + "&parse_mode=Markdown&text=" + send

   response = requests.get(send_text)
   return response.json()


site_url = "https://sam.sliitacademy.lk/"

content = get_div_class(site_url)
title = get_h3_class(site_url)
time = get_time_element(site_url)

if content is not None and title is not None and time is not None:
    num = 0
    for i in range(3):
        num = num + 1
        notice_content = str(content[i])
        notice_title = str(title[i])
        notice_time = str(time[i])

        output = f'''
        *SITE ANNOUNCEMENT {num} 🔴*

        *{notice_title}*
        _{notice_time}_
        {'-'*50}
        {notice_content}

        {'-'*50}
        _SLIIT Moodle Alert System - v1.2.0_
        _Copyright (c) Ashfaaq Rifath_'''

        print(output)
        telegram_notification(output)
else:
    print("error")
