import os
import time
import threading
import subprocess
import telebot
import requests
from bs4 import BeautifulSoup
from plyer import notification


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

def telegram_alert(send):
    bot_token = "BOT TOKEN"
    my_chatID = "CHAT ID"
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + my_chatID + "&parse_mode=Markdown&text=" + send

    response = requests.get(send_text)
    return response.json()

###########################################################################
pid = os.getpid()

notification.notify(
    title="Moodle Alert System",
    message=f'''Program running in the background
Process ID: {pid}''',
    app_icon=None,
    timeout=5,)

with open("mas_pid.txt", "w") as f:
    f.write(f"Moodle Alert System process ID: {str(pid)}")
    f.close()

###########################################################################

bot = telebot.TeleBot("BOT TOKEN")
@bot.message_handler(func=lambda message: True)

def command_engine(message):
    if message.text.lower() == "start":

        site_url = "https://sam.sliitacademy.lk/"
        content = get_div_class(site_url)
        title = get_h3_class(site_url)
        time_stamp = get_time_element(site_url)

        if content is not None and title is not None and time_stamp is not None:
            num = 4
            for i in range(2, -1, -1):
                num = num - 1
                notice_content = str(content[i])
                notice_title = str(title[i])
                notice_time = str(time_stamp[i])
                output = f'''
                *SITE ANNOUNCEMENT {num} 🔴*

                *{notice_title}*
                _{notice_time}_
                {'-'*50}
                {notice_content}

                {'-'*50}
                _SLIIT Moodle Alert System - v1.5_
                _Copyright (c) Ashfaaq Rifath_'''

                telegram_alert(output)
        else:
            bot.reply_to(message, "Error")

    elif message.text.lower() == "stop":
        notification.notify(
        title="Moodle Alert System",
        message="Program Termianted",
        app_icon=None,
        timeout=5,)

        bot.reply_to(message, "Program Terminated")
        subprocess.run(["taskkill", "/F", "/PID", str(pid)])
    else:
        bot.reply_to(message, "Invalid Command")

def telegram_bot():
    while True:
        try:
            bot.polling()
        except:
            #print("bot")
            time.sleep(5)

def moodle_alert_system():
    while True:
        try:
            site_url = "https://sam.sliitacademy.lk/"

            content = get_div_class(site_url)
            title = get_h3_class(site_url)
            time_stamp = get_time_element(site_url)

            if content is not None and title is not None and time_stamp is not None:
                num = 4
                for i in range(2, -1, -1):
                    num = num - 1
                    notice_content = str(content[i])
                    notice_title = str(title[i])
                    notice_time = str(time_stamp[i])

                    output = f'''
                    *SITE ANNOUNCEMENT {num} 🔴*

                    *{notice_title}*
                    _{notice_time}_
                    {'-'*50}
                    {notice_content}

                    {'-'*50}
                    _SLIIT Moodle Alert System - v1.5_
                    _Copyright (c) Ashfaaq Rifath_'''

                    telegram_alert(output)
                time.sleep(3600)
            else:
                quit()
        except:
            #print("Working...")
            time.sleep(300)

telegram_bot_thread = threading.Thread(target=telegram_bot)
telegram_bot_thread.start()
moodle_alert_system()
telegram_bot_thread.join()
