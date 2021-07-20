import unittest
from selenium import webdriver
import os

class AvtoDispetcherTest(unittest.TestCase):
    def setUp(self):
        if os.uname == 'Linux':
            self.driver = webdriver.Chrome("/webdrivers/chromedriver")
            self.driver.get("https://yandex.ru/")
        if os.uname == "Windows":
            self.driver = webdriver.Chrome("/webdrivers/chromedriver.exe")
            self.driver.get("https://yandex.ru/")


    def test_check_yandex(self):
        pass
    

    def test_enter_question(self):
        pass


    def test_results_yandex(self):
        pass
    

    def test_find_result(self):
        pass
    

    def test_route_to_autodispatsher(self):
        pass
    

    def test_check_autodispatcher(self):
        pass
    

    def test_enter_data(self):
        pass
    
    
    def test_results_1(self):
        pass
    

    def test_results_1(self):
        pass

    def test_enter_new_data(self):
        pass
    

    def test_results_2(self):
       pass
    

    # #Testing Single Input Field.    
    # def test_singleInputField(self):
    #     pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get(pageUrl)

    #     #Finding "Single input form" input text field by id. And sending keys(entering data) in it.
    #     eleUserMessage = driver.find_element_by_id("user-message")
    #     eleUserMessage.clear()
    #     eleUserMessage.send_keys("Test Python")

    #     #Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
    #     eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
    #     eleShowMsgBtn.click()

    #     #Checking whether the input text and output text are same using assertion.
    #     eleYourMsg=driver.find_element_by_id("display")
    #     assert "Test Python" in eleYourMsg.text
 
    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()