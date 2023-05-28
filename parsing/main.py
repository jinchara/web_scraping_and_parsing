import requests
import csv
from time import sleep
from random import randint
from bs4 import BeautifulSoup

payloads = {'sort': 'MostVotes', 'edited': 'true', 'tab': 'votes', 'page': 1, 'pagesize': '15'}
url = 'https://stackoverflow.com/questions'
headers = {'Accept-Language': 'en-US'}
file = open('stack_questions.csv', 'w', newline='', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['Questions','Views','Votes'])
while payloads['page'] <= 4:
    response = requests.get(url, params=payloads, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    posts_soup = soup.find('div', class_="flush-left")
    all_posts = posts_soup.find_all('div', class_="s-post-summary")

    for posts in all_posts:
        vote = posts.span.text
        div_element = posts.find("div", class_="s-post-summary--stats-item is-supernova")
        views = div_element["title"]
        views = views.replace("views", "").strip()
        question = posts.a.text
        print(question, views, vote)
        if "," in question:
            question = question.replace(",", " ")
        csv_obj.writerow([question, views, vote])

    payloads['page'] += 1
    sleep(randint(15, 20))
