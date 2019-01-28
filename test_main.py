# -*- coding: utf-8 -*-
import re
import csv
import unittest
import locators as lc
from time import sleep
from testconfig import config
from selenium import webdriver
from parameterized import parameterized
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


# Decrease logging level in trace_back
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)
LOC = lc.Main()

main_url = 'https://docdoc.ru'
doc_url = main_url + '/doctor'


# cases_list = []
# with open('./params.csv', 'rb') as cases:
#     reader = csv.reader(cases)
#     for row in reader:
#         if len(row) == 4:
#             cases_list.append(row)
#         else:
#             raise Exception('Wrong format for "params.csv". '
#                             'Must be 4th values per row for scheme: FROM, TO, VALUE, RESULT')


class MainTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.osb = config.get('osb')
        cls.browser = config.get('browser')
        print cls.osb, cls.browser
        if cls.browser == 'firefox':
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

        cls.driver.implicitly_wait(2)

    def test_main(cls):
        d = cls.driver
        d.get(doc_url)
        dropdown = LOC.dropdown(d)
        print dropdown.text
        dropdown.click()
        sleep(3)

    # @parameterized.expand(cases_list)
    # def test_currencies_change(cls, cur_from, cur_to, cur_value, cur_expected_result):
    #     d = cls.driver
    #     d.get(host)
    #     # switch the currencies types
    #     currency_from = LOC.currency_from(d)
    #     currency_from.click()
    #     dropdown_currency_from = LOC.currency_dropdown(d, cur_from)
    #     dropdown_currency_from.click()
    #     currency_to = LOC.currency_to(d)
    #     currency_to.click()
    #     dropdown_currency_to = LOC.currency_dropdown(d, cur_to)
    #     dropdown_currency_to.click()
    #     # send the currencies values
    #     currency_value_input = LOC.input_sum(d)
    #     currency_value_input.click()
    #     currency_value_input.clear()
    #     currency_value_input.send_keys(cur_value)
    #     # check the answer result
    #     get_result = LOC.result_button(d)
    #     get_result.click()
    #     sleep(2)
    #     if bool(cur_expected_result) == True:
    #         try:
    #             result_total = LOC.result_answer(d)
    #             assert result_total.is_displayed(), \
    #                 'Conversion result did not provided.\nCase: from {value} {from_} to {to_}'.format(value=cur_value,
    #                                                                                                   from_=cur_from,
    #                                                                                                   to_=cur_to)
    #         except TimeoutException:
    #             cls.fail(
    #                 'Conversion result did not provided.\nCase: from {value} {from_} to {to_}'.format(value=cur_value,
    #                                                                                                   from_=cur_from,
    #                                                                                                   to_=cur_to))
    #
    # def test_old_period_change(cls):
    #     '''
    #     dalee send_keys(Keys.BACKSPACE) - kostili 4tobi skinut daty na samuyu rannuu,
    #     ibo polya dlya vvoda dat o4en krivie i bez podderjki ru4nogo vvoda, send_keys v nih ne rabotaet,
    #     a slojniu obvyazky dlya etogo datepicker'a pisat mne prosto len
    #     '''
    #     d = cls.driver
    #     d.get(host)
    #     earliest_txt = LOC.earliest_period(d).text
    #     earliest_date = re.findall(r"(\d.+)", earliest_txt)[0]
    #     date_start = LOC.date_start(d)
    #     date_start.click()
    #     date_start.send_keys(Keys.BACKSPACE)
    #     date_end = LOC.date_end(d)
    #     date_end.click()
    #     date_end.send_keys(Keys.BACKSPACE)
    #     period_button = LOC.period_button(d)
    #     period_button.click()
    #     sleep(2)
    #     try:
    #         no_data = LOC.no_data(d)
    #         assert no_data.is_displayed() == False, 'There is an missing-data error on the date: ' \
    #                                                 '{calenda}, but it must be'.format(calenda=earliest_date)
    #
    #         graph = LOC.graph(d)
    #         assert graph.is_displayed() == True, 'It seems no graphics on the date: {calenda}, but it must be'.format(
    #             calenda=earliest_date)
    #     except TimeoutException:
    #         cls.fail('It seems no graphics on the date: {calenda}, but it must be'.format(calenda=earliest_date))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
