# -*- coding: utf-8 -*-
import unittest
import locators as lc
from time import sleep
from testconfig import config
from selenium import webdriver
# Decrease logging level in trace_back
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)
LOC = lc.Main()

main_url = 'https://docdoc.ru'
doc_url = main_url + '/doctor'


class MainTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.osb = config.get('osb')
        cls.browser = config.get('browser')
        if cls.browser in ['firefox', 'Firefox', 'mozilla', 'Mozilla']:
            moz_options = webdriver.FirefoxOptions()
            moz_options.add_argument("--no-sandbox")
            if cls.osb in ['macos', 'MacOS']:
                cls.driver = webdriver.Firefox(firefox_options=moz_options, executable_path='./geckodriver_macos')
            elif cls.osb in ['windows', 'Windows']:
                cls.driver = webdriver.Firefox(firefox_options=moz_options, executable_path='./geckodriver64.exe')
            else:
                cls.driver = webdriver.Firefox(firefox_options=moz_options, executable_path='./geckodriver_unix64')
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            if cls.osb in ['macos', 'MacOS']:
                cls.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver_macos')
            elif cls.osb in ['windows', 'Windows']:
                cls.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver32.exe')
            else:
                cls.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver_unix64')

        cls.driver.implicitly_wait(3)

    def test_main(cls):
        d = cls.driver
        d.get(doc_url)

        # Check default filter value
        dropdown_default, expected_text = LOC.dropdown_button_default(d)
        d.execute_script('return arguments[0].scrollIntoView();', dropdown_default)
        assert dropdown_default.text == expected_text, \
            'Некорректный текст заголовка в фильтре дропдауна по дефолту.\n' \
            'Получено: {got}\nОжидаемо: {exp}'.format(got=dropdown_default.text.encode('utf-8'), exp=expected_text)

        # Trying to open filter popup. Not stable. Kostily added
        dropdown_default.click()
        dropdown_opened = LOC.dropdown_opened(d)
        if dropdown_opened is False:
            dropdown_default.click()
            dropdown_opened = LOC.dropdown_opened(d)
            if dropdown_opened is False:
                dropdown_default.click()
        # Asserting popup filter was opened
        dropdown_opened = LOC.dropdown_opened(d)
        assert dropdown_opened is True, \
            'Дропдаун выбора фильтров не раскрылся'

        # Checking amount of default active filters
        dropdown_filters_active, expected_text = LOC.dropdown_value_default_active(d)
        assert len(dropdown_filters_active) == 1, \
            'Некорректное число активных фильтров в дропдауне по дефолту.\n' \
            'Получено: {got}\nОжидаемо: 1'.format(got=len(dropdown_filters_active))

        # Checking value of a default active filter
        assert dropdown_filters_active[0].text == expected_text, \
            'Некорректный текст фильтра в дропдауне.\n' \
            'Получено: {got}\nОжидаемо: {exp}'.format(got=dropdown_filters_active[0].text.encode('utf-8'), exp=expected_text)

        # Checking default active filter has a selecting mark
        default_mark = LOC.dropdown_value_marker_displayed(dropdown_filters_active[0])
        assert default_mark is True, \
            'Маркер выбранного фильтра не найден для дефолтного фильтра.\n'
        dropdown_value_tomorrow, expected_text = LOC.dropdown_value_tomorrow(d)

        # Checking Tomorrow text value in a dropdown.
        try:
            tomorrow_text = dropdown_value_tomorrow.text.split(', ')[0]
            assert tomorrow_text == expected_text,  \
                'Некорректный текст фильтра в дропдауне.\n' \
                'Получено: {got}\nОжидаемо: {exp}'.format(got=tomorrow_text.encode('utf-8'), exp=expected_text)
        except Exception as err:
            cls.fail('Ошибка при получении значения фильтра "Завтра", {}'.format(err))

        # Checking Tomorrow text applied to a filter header value
        dropdown_value_tomorrow.click()
        dropdown_button_tomorrow, expected_text = LOC.dropdown_button_tomorrow(d)
        assert dropdown_button_tomorrow.text == expected_text,  \
            'Некорректный текст заголовка в фильтре после выбора "Завтра".\n' \
            'Получено: {got}\nОжидаемо: {exp}'.format(got=dropdown_button_tomorrow.text.encode('utf-8'), exp=expected_text)
        sleep(3)

        # Checking elements on page after a page reload
        # Focus on the page results element
        resss = d.find_element_by_class_name('the-doctor-list-items')
        d.execute_script('return arguments[0].scrollIntoView();', resss)

        # Checking a Tomorrow value has a selected mark. The same kostyls here.
        dropdown_button_tomorrow.click()
        dropdown_opened = LOC.dropdown_opened(d)
        if dropdown_opened is False:
            dropdown_button_tomorrow.click()
            dropdown_opened = LOC.dropdown_opened(d)
            if dropdown_opened is False:
                dropdown_button_tomorrow.click()
        dropdown_value_tomorrow, expected_text = LOC.dropdown_value_tomorrow(d)
        tomorrow_mark = LOC.dropdown_value_marker_displayed(dropdown_value_tomorrow)
        assert tomorrow_mark is True, \
            'Маркер выбранного фильтра не найден после смены фильтра.\n'
        # Focus on the page results element
        resss = d.find_element_by_class_name('the-doctor-list-items')
        d.execute_script('return arguments[0].scrollIntoView();', resss)

        # Checking a grid with results has a correct default length
        results, expected_lenght = LOC.results(d)
        assert len(results) == expected_lenght,  \
            'Некорректное число результатов выдачи после смены фильтра.\n' \
            'Получено: {got}\nОжидаемо: 10'.format(got=len(dropdown_filters_active))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
