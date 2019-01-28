# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Main():



    def await_element(self, driver, time, method, select):
        WebDriverWait(driver, time).until(ec.presence_of_all_elements_located((method, select)))

        return driver.find_element(method, select)

    def await_elements(self, driver, time, method, select):
        WebDriverWait(driver, time).until(ec.presence_of_all_elements_located((method, select)))

        return driver.find_elements(method, select)

    def dropdown(self, driver):
        method = By.CSS_SELECTOR
        select = "div[data-test-id='date_filter']"

        element = self.await_element(driver, 2, method, select)

        return element

    # def input_sum(self, driver):
    #     method = By.CSS_SELECTOR
    #     select = "*[class$='right input']"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0].find_element_by_xpath('//input[@placeholder="Сумма"]')
    #
    #     return element
    #
    # def currency_from(self, driver):
    #     method = By.CSS_SELECTOR
    #     select = "header[data-popup-initialized]"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0]
    #
    #     return element
    #
    # def currency_to(self, driver):
    #     method = By.CSS_SELECTOR
    #     select = "header[data-popup-initialized]"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[1]
    #
    #     return element
    #
    # def result_button(self, driver):
    #     method = By.CSS_SELECTOR
    #     select = "button.rates-button"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0]
    #     driver.execute_script('return arguments[0].scrollIntoView();', element)
    #
    #     return element
    #
    # def result_answer(self, driver):
    #     method = By.CSS_SELECTOR
    #     select = "div[class='rates-converter-result__total']"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0]
    #
    #     return element
    #
    # def currency_dropdown(self, driver, currency):
    #     method = By.CSS_SELECTOR
    #     select = "div[class='visible']"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0].find_element_by_xpath(".//*[text()[contains(.,'{cur}')]]".format(cur=currency))
    #     driver.execute_script('return arguments[0].scrollIntoView();', element)
    #
    #     return element
    #
    # def earliest_period(self, driver):
    #     method = By.CSS_SELECTOR
    #     select = "div[class='rates-details__notes print-invisible']"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0]
    #
    #     return element
    #
    # def date_start(self, driver):
    #     method = By.XPATH
    #     select = "//*[@data-property='fromDate']"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0]
    #
    #     return element
    #
    # def date_end(self, driver):
    #     method = By.XPATH
    #     select = "//*[@data-property='toDate']"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0]
    #
    #     return element
    #
    # def period_button(self, driver):
    #     method = By.CSS_SELECTOR
    #     select = "*[class$='filter-button']"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0]
    #
    #     return element
    #
    # def graph(self, driver):
    #     method = By.CSS_SELECTOR
    #     select = "*[class$='jqplot-event-canvas']"
    #
    #     elements = self.await_element(driver, method, select)
    #     element = elements[0]
    #     driver.execute_script('return arguments[0].scrollIntoView();', element)
    #
    #     return element
    #
    # def no_data(self, driver):
    #     method = By.XPATH
    #     select = ".//*[text()='{pew}']/..".format(pew=Main.miss_data_exp_text.encode('utf-8'))
    #
    #     try:
    #         element = driver.find_element(method, select)
    #         driver.execute_script('return arguments[0].scrollIntoView();', element)
    #
    #         return element
    #     except Exception:
    #
    #         return True