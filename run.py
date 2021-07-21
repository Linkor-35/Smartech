from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import re
from sys import platform


PATH_LINUX = os.getcwd() + "/webdrivers/chromedriver"
# PATH_WIN = "/webdrivers/chromedriver.exe"


DRIVER = None


def open_yandex_url():
    """Пользователь заходит на сайт Яндекс: www.yandex.ru"""
    global DRIVER
    if platform == 'linux':
        DRIVER = webdriver.Chrome(PATH_LINUX)
        DRIVER.maximize_window()
        DRIVER.get("https://yandex.ru/")

    # if platform == "win32":
    #     DRIVER = webdriver.Chrome(PATH_WIN)
    #     DRIVER.get("https://yandex.ru/")



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
            return True


def go_to_curent_url():
    """Найдя нужный результат с этого сайта – пользователь кликает на данном результате и переходит на сайт www.avtodispetcher.ru/distance/ """
    elems = DRIVER.find_elements_by_tag_name('a')
    for elem in elems:
        href = elem.get_attribute('href')
        if href == "https://www.avtodispetcher.ru/distance/":
            elem.click()
            break

   
def enter_locations():
    """5. Убедившись, что открылась верная ссылка, пользователь вводит следующие значения в поля:
        a. Поле «Откуда» - «Тула»
        b. Поле «Куда» - «Санкт-Петербург»
        c. Поле «Расход топлива» - «9»
        d. Поле «Цена топлива» - «46»"""
    global DRIVER
    # тут нужно запилить проверку на корректность ссылки. туда ли пришел
    tabs = DRIVER.window_handles
    DRIVER.switch_to.window(tabs[1])

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


def check_results():
    """Пользователь проверяет что рассчитанное расстояние = 897 км, а стоимость топлива = 3726 руб."""
    current_distance = 897
    current_fuel = 3726
    time.sleep(5)
    result = DRIVER.find_element_by_id("summaryContainer").text
    distance = int(re.search(r"Расстояние: \d*", result).group(0).split(" ")[-1])
    fuel = int(re.search(r"= \d* руб", result).group(0).split(" ")[-2])
    if current_distance == distance and current_fuel == fuel:
        print("First result is current")
        return True
    else:
        return False


def click_change_trip():
    """Пользователь кликает на «Изменить маршрут»"""
    # нет кнопки Изменить маршрут есть кнопка 
    change = DRIVER.find_element_by_class_name("anchor")
    change.click()


def enter_new_trip():
    """В открывшейся форме в поле «Через города» вводит «Великий Новгород» 
    Ждет 30 секунд и снова нажимает «Рассчитать»"""
    in_destination = DRIVER.find_element_by_xpath("//*[@id='inter_points_field_parent']/input")
    in_destination.send_keys("Великий Новгород")
    time.sleep(30)
    in_destination.send_keys(Keys.ENTER)


def check_new_results():
    """Пользователь проверяет что расстояние теперь = 966 км, а стоимость топлива = 4002 руб."""
    current_distance = 966
    current_fuel = 4002
    result = DRIVER.find_element_by_id("summaryContainer").text
    distance = int(re.search(r"Расстояние: \d*", result).group(0).split(" ")[-1])
    fuel = int(re.search(r"= \d* руб", result).group(0).split(" ")[-2])
    if current_distance == distance and current_fuel == fuel:
        print("Sekond result is current")
        return True
    else:
        return False
    

def close_ssesion():
    DRIVER.quit()
    """12. В пункты 7 и 11 добавить валидацию построенной карты в дополнение к численному расчету.
    13. После запуска сценария должен генерироваться отчет, в котором будет содержаться информация
    о выполненном тесте и скриншоты ошибок и результирующих расчетов чтобы пользователь мог 
    проверить корректность выполнения теста. """


def main():
    open_yandex_url()
    enter_question()
    if find_curent_url() == True:
        go_to_curent_url()
        enter_locations()
        click_find_result()
    if check_results() == True:
        click_change_trip()
        enter_new_trip()
        if check_new_results() == True:
            print("ALL test is DONE")
        close_ssesion()

    if find_curent_url == False:
        DRIVER.quit()


if __name__ == "__main__":
    main()
