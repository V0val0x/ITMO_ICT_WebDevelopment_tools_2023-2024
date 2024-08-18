import multiprocessing
import time
import requests
from bs4 import BeautifulSoup
from connection import DBConn
from data import URLs, number_of_threads


def parse_and_save_multiprocessing(url):
    db_conn = DBConn.connect_to_database()
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')  # создаем парсер
        articles = soup.find_all('article', class_='tm-articles-list__item')
        for article in articles:
            author = article.find('a', class_='tm-user-info__username').text
            datetime = article.find('a', class_='tm-article-datetime-published tm-article-datetime-published_link').text
            title = article.find('a', class_='tm-title__link').text

            with db_conn.cursor() as cursor:  # через специальный класс cursor получаем доступ к базе данных
                cursor.execute(DBConn.INSERT_SQL, (title, author, datetime))

        db_conn.commit()
    except Exception as e:
        print("Ошибка:", e)
        db_conn.rollback()
    finally:
        db_conn.close()


def process_url_list_multiprocessing(url_list):
    for url in url_list:
        parse_and_save_multiprocessing(url)


def main_multiprocessing():
    chunk_size = len(URLs) // number_of_threads
    url_chunks = [URLs[i:i + chunk_size] for i in range(0, len(URLs), chunk_size)]

    processes = []
    for chunk in url_chunks:
        process = multiprocessing.Process(target=process_url_list_multiprocessing, args=(chunk,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    start_time = time.time()
    main_multiprocessing()
    end_time = time.time()
    print(f"Время выполнения multiprocessing: {end_time - start_time} секунд")
