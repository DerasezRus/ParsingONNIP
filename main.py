#                           Инструкция для разработчика
# Если вы запустили первый раз PyChar
# Нужно установить библиотек: 1)lxml 2)requests 3)Beautifulsoup4 4)pandas
#                                   Пример - pip install requests


# Библиотеки
import requests
from bs4 import BeautifulSoup

# Классы, которыми пользуемся в Main
from write_txt import write_txt
from write_excel import write_excel

# Ocновной класс
class Parsing:

    # Пустой метод
    def __init__(self):
        pass

    # Переменные
    # URL - ссылка на сайт, response - сохраняем данные, soup - помещаем текст ответа
    URL = 'https://iotvega.com/product'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'lxml')

    # Теги, которые хотим парсить
    div_product_name = soup.find_all('div', class_='product-name')
    div_product_items = soup.find_all('a', class_='main-container')

    # Ключевые слова, по которым ищем информацию в features = i.find('ul').text.strip()
    search_word = ('Датчик', 'датчик', 'базовая станция', 'Базовая станция')

    # Счётчик для сохранения данных в write_txt
    count = 0

    # Списки в которые будут записываться данные с тегов
    list_product = []
    list_features = []
    list_money = []

    # Списки для сохранения в словарь и файл write_txt "data.txt"
    ready_dictionary = {}
    ready_list = []

    # Цикл всех тегов на сайте
    for n, i in enumerate(div_product_items, start=1):

        # Запись тегов в переменные
        product = i.find('h2').text
        features = i.find('ul').text.strip()
        money = i.find('span').text.strip()

        # Цикл на проверку ключевых слов
        for word in range(len(search_word)):
            # Цикл перебора слов из списка search_word
            if features.find(search_word[word]) != -1:
                # Условия, чтобы не выводилась информация с money
                if money == 'Снято с продажи' or money == 'Цена по запросу':
                    pass
                else:
                    # Добавление данных в списки
                    list_product.append(product)
                    list_features.append(features)
                    list_money.append(money)
                    list_money.sort()
                    count += 1

    # Вызовов метода из класса write_txt
    write_txt.write_txt(list_product, list_features, list_money, count, ready_dictionary)

    # Вызовов метода из класса write_excel
    write_excel.write_excel(list_product, list_features, list_money)

