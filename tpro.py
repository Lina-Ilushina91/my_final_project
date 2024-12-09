import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TproSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search_in_tpro_by(self): # функция
        driver = self.driver
        driver.get("https://tpro.by/") # переход на сайт
        elem = driver.find_element(By.NAME, "q")      # проверка в поисковой строке кода и значения name
        time.sleep(4)
        elem.send_keys("абракадабра")
        time.sleep(4)
        elem.send_keys(Keys.RETURN)
        time.sleep(4)
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        time.sleep(4)
        elem.send_keys("пила")
        time.sleep(4)
        elem.send_keys(Keys.RETURN)
        time.sleep(4)
        self.assertNotIn("По вашему запросу ничего не найдено.", driver.page_source)



    def test_login_tpro(self):
        driver = self.driver
        driver.get("https://tpro.by/auth/")
        time.sleep(5)
        elem = driver.find_element(By.LINK_TEXT, "Вход")
        elem.click()
        time.sleep(5)
        elem = driver.find_element(By.XPATH, "//input[@name='USER_LOGIN']")
        elem.send_keys("Alina")
        time.sleep(5)
        elem = driver.find_element(By.XPATH, "//input[@name='USER_PASSWORD']")
        elem.send_keys("12345May")
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("Личный кабинет", driver.page_source)
        time.sleep(5)
        print(driver.page_source)
        driver.get("https://tpro.by/exit/")
        time.sleep(5)


    def tearDown(self):
        self.driver.close() # закрытие браузера по окончанию теста







if __name__ == '__main__':
    unittest.main()
