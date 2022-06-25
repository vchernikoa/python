'''
1. Открыть страницу http://google.com/ncr
2. Выполнить поиск слова “selenide”
3. Проверить, что первый результат – ссылка на сайт selenide.org.
4. Перейти в раздел поиска изображений
5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
6. Вернуться в раздел поиска Все
7. Проверить, что первый результат такой же, как и на шаге 3.
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')
        self.drv.get('http://www.google.com')

    def test_seatch(self):
        elem = self.drv.find_element_by_name('q')
        elem.send_keys('selenide')
        elem.send_keys(Keys.RETURN)

        elem = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite')
        if 'selenide.org' in elem.text:
            print('Шаг 3: Первая ссылка соответствует запросу')

        elem = self.drv.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        elem.click()

        elem = self.drv.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]/span')
        assert 'selenide' in self.drv.title
        print('Шаг 5: Картинка соответсвует')

        elem = self.drv.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
        elem.click()

        elem = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite')
        if 'selenide.org' in elem.text:
            print('Шаг 7: Первая ссылка соответствует запросу')

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()
