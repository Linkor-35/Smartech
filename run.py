from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os


PATH_LINUX = os.getcwd() + "/webdrivers/chromedriver"
PATH_WIN = "/webdrivers/chromedriver.exe"
OS = os.uname()
# caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"

DRIVER = None


def open_yandex_url():
    """Пользователь заходит на сайт Яндекс: www.yandex.ru"""
    global DRIVER
    if OS.sysname == 'Linux':
        DRIVER = webdriver.Chrome(PATH_LINUX)
        DRIVER.get("https://yandex.ru/")
    if OS.sysname == "Windows":
        DRIVER = webdriver.Chrome(PATH_WIN)
        DRIVER.get("https://yandex.ru/")
    


def enter_question():
    """Вводит в поисковую строку фразу «расчет расстояний между городами» и запускает поиск"""
    search = DRIVER.find_element_by_id("text")
    search.send_keys("расчет расстояний между городами")
    search.send_keys(Keys.RETURN)


def find_curent_url():
    elems = DRIVER.find_elements_by_tag_name('a')
    for elem in elems:
        href = elem.get_attribute('href')
        if href == "https://www.avtodispetcher.ru/distance/":
            return elem


def go_to_curent_url(elem):
    """Найдя нужный результат с этого сайта – пользователь кликает на данном результате и переходит на сайт www.avtodispetcher.ru/distance/ """
    if elem:
        elem.click()
        return elem

   
def enter_locations():
    """5. Убедившись, что открылась верная ссылка, пользователь вводит следующие значения в поля:
        a. Поле «Откуда» - «Тула»
        b. Поле «Куда» - «Санкт-Петербург»
        c. Поле «Расход топлива» - «9»
        d. Поле «Цена топлива» - «46»"""
    global DRIVER
    # тут нужно запилить проверку на корректность ссылки. туда ли пришел
    DRIVER.switch_to_window(window_name=DRIVER.window_handles[0])
    DRIVER.close()
    DRIVER.switch_to_window(window_name=DRIVER.window_handles[0])

    start_point = DRIVER.find_element_by_name("from")
    start_point.send_keys("Тула")

    end_point = DRIVER.find_element_by_name("to")
    end_point.send_keys("Санкт-Петербург")

    fuel = DRIVER.find_element_by_name("fc")
    fuel.send_keys(Keys.CONTROL + "a")
    fuel.send_keys("9")

    fuel = DRIVER.find_element_by_name("fp")
    fuel.send_keys(Keys.CONTROL + "a")
    fuel.send_keys("46")


def click_find_result():
    """Пользователь нажимает кнопку «Рассчитать» """
    submit = DRIVER.find_element_by_class_name("submit_button")
    submit.click()
    time.sleep(10)


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
    elem = find_curent_url()
    if elem:
        go_to_curent_url(elem)
        enter_locations()
        click_find_result()
    if not elem:
        DRIVER.quit()

    # global DRIVER
    # DRIVER = webdriver.Chrome(PATH_LINUX)
    # DRIVER.get("https://www.avtodispetcher.ru/distance/")
    
    # check_results()
    # click_change_trip()
    # enter_new_trip()
    # check_new_results()
    close_ssesion()
    


if __name__ == "__main__":
    main()