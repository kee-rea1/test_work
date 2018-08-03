# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Main():

    hostname = 'http://www.sberbank.ru/ru/quotes/converter'
    exp_text = u'Вы получите:'
    miss_data_exp_text = u'Для этой валюты по указанным параметрам нет данных'

    def awaiter(self, driver, method, select):
        WebDriverWait(driver, 2).until(ec.presence_of_all_elements_located((method, select)))

        return driver.find_elements(method, select)

    def input_sum(self, driver):
        method = By.CSS_SELECTOR
        select = "*[class$='right input']"

        elements = self.awaiter(driver, method, select)
        element = elements[0].find_element_by_xpath('//input[@placeholder="Сумма"]')

        return element

    def currency_from(self, driver):
        method = By.CSS_SELECTOR
        select = "header[data-popup-initialized]"

        elements = self.awaiter(driver, method, select)
        element = elements[0]

        return element

    def currency_to(self, driver):
        method = By.CSS_SELECTOR
        select = "header[data-popup-initialized]"

        elements = self.awaiter(driver, method, select)
        element = elements[1]

        return element

    def result_button(self, driver):
        method = By.CSS_SELECTOR
        select = "button.rates-button"

        elements = self.awaiter(driver, method, select)
        element = elements[0]
        driver.execute_script('return arguments[0].scrollIntoView();', element)

        return element

    def result_answer(self, driver):
        method = By.CSS_SELECTOR
        select = "div[class='rates-converter-result__total']"

        elements = self.awaiter(driver, method, select)
        element = elements[0]

        return element

    def currency_dropdown(self, driver, currency):
        method = By.CSS_SELECTOR
        select = "div[class='visible']"

        elements = self.awaiter(driver, method, select)
        element = elements[0].find_element_by_xpath(".//*[text()[contains(.,'{cur}')]]".format(cur=currency))
        driver.execute_script('return arguments[0].scrollIntoView();', element)

        return element

    def earliest_period(self, driver):
        method = By.CSS_SELECTOR
        select = "div[class='rates-details__notes print-invisible']"

        elements = self.awaiter(driver, method, select)
        element = elements[0]

        return element

    def date_start(self, driver):
        method = By.XPATH
        select = "//*[@data-property='fromDate']"

        elements = self.awaiter(driver, method, select)
        element = elements[0]

        return element

    def date_end(self, driver):
        method = By.XPATH
        select = "//*[@data-property='toDate']"

        elements = self.awaiter(driver, method, select)
        element = elements[0]

        return element

    def period_button(self, driver):
        method = By.CSS_SELECTOR
        select = "*[class$='filter-button']"

        elements = self.awaiter(driver, method, select)
        element = elements[0]

        return element

    def graph(self, driver):
        method = By.CSS_SELECTOR
        select = "*[class$='jqplot-event-canvas']"

        elements = self.awaiter(driver, method, select)
        element = elements[0]
        driver.execute_script('return arguments[0].scrollIntoView();', element)

        return element

    def no_data(self, driver):
        method = By.XPATH
        select = ".//*[text()='{pew}']/..".format(pew=Main.miss_data_exp_text.encode('utf-8'))

        try:
            element = driver.find_element(method, select)
            driver.execute_script('return arguments[0].scrollIntoView();', element)

            return element
        except Exception:

            return True