from bs4 import BeautifulSoup
import requests

skillbox = requests.get("https://live.skillbox.ru/") # Получаем ответ от сайта скиллбокс
print(skillbox.status_code)

skillsoup = BeautifulSoup(skillbox.content, "html.parser") # Разбираем код страницы на элементы
webinars = skillsoup.findAll(class_ = "webinar-card__title") # Находим все элемены с указаным классом
print([webinar.string.strip() for webinar in webinars])

# Попробуем сделать парсинг по сложнее, получим еще и даты проведения
webinarsFull = skillsoup.findAll(class_ = "webinars__item")
print("---------------------------------------------------------------")
for webinar in webinarsFull:
    # Код обработки каждого вебинара
    title = webinar.find(class_ = "webinar-card__title").string.strip()
    date = webinar.find(class_ = "webinar-card__date").string.strip()
    print(f"Вебинар {title} прошел {date}")
