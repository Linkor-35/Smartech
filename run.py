from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


PATH_LINUX = os.getcwd() + "/webdrivers/chromedriver"
PATH_WIN = "/webdrivers/chromedriver.exe"
OS = os.uname()
DRIVER = None


def open_yandex_url():
    global DRIVER
    """Пользователь заходит на сайт Яндекс: www.yandex.ru"""
    if OS.sysname == 'Linux':
        DRIVER = webdriver.Chrome(PATH_LINUX)
    if OS.sysname == "Windows":
        DRIVER = webdriver.Chrome(PATH_WIN)
    DRIVER.get("https://yandex.ru/")
    title = DRIVER.title


def enter_question():
    """Вводит в поисковую строку фразу «расчет расстояний между городами» и запускает поиск"""
    search = DRIVER.find_element_by_id("text")
    search.send_keys("расчет расстояний между городами")
    search.send_keys(Keys.RETURN)


def find_curent_url():
    current_url = None
    elems = DRIVER.find_elements_by_tag_name('a')
    for elem in elems:
        href = elem.get_attribute('href')
        if href == "https://www.avtodispetcher.ru/distance/":
            current_url = elem
            break
    return current_url


def go_to_curent_url(url):
    """Найдя нужный результат с этого сайта – пользователь кликает на данном результате и переходит на сайт www.avtodispetcher.ru/distance/ """
    if url:
        curent_url = DRIVER.get("https://www.avtodispetcher.ru/distance/")
    time.sleep(5)
    
    

# def enter_locations():
#     """5. Убедившись, что открылась верная ссылка, пользователь вводит следующие значения в поля:
#         a. Поле «Откуда» - «Тула»
#         b. Поле «Куда» - «Санкт-Петербург»
#         c. Поле «Расход топлива» - «9»
#         d. Поле «Цена топлива» - «46»"""
#     pass


# def click_find_result():
#     """Пользователь нажимает кнопку «Рассчитать» """
#     pass


# def check_results():
#     """Пользователь проверяет что рассчитанное расстояние = 897 км, а стоимость топлива = 3726 руб."""
#     pass


# def click_change_trip():
#     """Пользователь кликает на «Изменить маршрут»"""
#     pass


# def enter_new_trip():
#     """В открывшейся форме в поле «Через города» вводит «Великий Новгород» 
#     Ждет 30 секунд и снова нажимает «Рассчитать»"""
#     pass


# def check_new_results():
#     """Пользователь проверяет что расстояние теперь = 966 км, а стоимость топлива = 4002 руб."""
#     pass


def close_ssesion():
    DRIVER.quit()
    """12. В пункты 7 и 11 добавить валидацию построенной карты в дополнение к численному расчету.
    13. После запуска сценария должен генерироваться отчет, в котором будет содержаться информация
    о выполненном тесте и скриншоты ошибок и результирующих расчетов чтобы пользователь мог 
    проверить корректность выполнения теста. """
    pass


def main():
    open_yandex_url()
    enter_question()
    url = find_curent_url()
    # global DRIVER
    # DRIVER = webdriver.Chrome(PATH_LINUX)
    # url = True
    go_to_curent_url(url)
    # enter_locations()
    # click_find_result()
    # check_results()
    # click_change_trip()
    # enter_new_trip()
    # check_new_results()
    close_ssesion()
    


if __name__ == "__main__":
    main()