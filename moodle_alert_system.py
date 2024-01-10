import requests
from bs4 import BeautifulSoup


def get_content(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")
    element = bs.find_all("article")[:3]

    article_list = []

    for article in element:
        article_list.append(article.text)
    return article_list
    
def telegram_notification(send):
   bot_token = "6585671034:AAEemxbzcNCaPv-xrKK1Ro3eedvqbV20gHc"
   my_chatID = "1813981055"
   send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + my_chatID + "&parse_mode=Markdown&text=" + send

   response = requests.get(send_text)
   return response.json()


site_url = "https://sam.sliitacademy.lk/"
content = get_content(site_url)

if content != None:
    i = 0
    for item in content:
        i = i + 1
        notice = str(item)

        output = f'''
        SITE ANNOUNCEMENTS - SLIITA
        NOTICE {i} 🔴
        {notice}
        {'='*30}
        Moodle Alert System - v1.0.0
        Copyright (c) Ashfaaq Rifath'''

        print(output)
        telegram_notification(output)
else:
    print("error")