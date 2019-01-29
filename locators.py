# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class Main():

    def await_vis_element(self, driver, time, method, select):
        WebDriverWait(driver, time).until(ec.visibility_of_element_located((method, select)))

        return driver.find_element(method, select)

    def await_element(self, driver, time, method, select):
        WebDriverWait(driver, time).until(ec.presence_of_element_located((method, select)))

        return driver.find_element(method, select)

    def await_elements(self, driver, time, method, select):
        WebDriverWait(driver, time).until(ec.presence_of_all_elements_located((method, select)))

        return driver.find_elements(method, select)

    def dropdown_button_default(self, driver):
        expected_text = u'Расписание на все дни'
        method = By.CSS_SELECTOR
        select = 'div[data-test-id="date_filter"]'
        element = self.await_element(driver, 4, method, select)
        element = element.find_element_by_css_selector('span[class=select-box__title]')

        return element, expected_text

    def dropdown_opened(self, driver):
        method = By.CSS_SELECTOR
        select = 'div[data-test-id="date_select_items"]'
        try:
            self.await_vis_element(driver, 1, method, select)
            return True
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            return False

    def dropdown_value_default_active(self, driver):
        expected_text = u'Все дни'
        method = By.CSS_SELECTOR
        select = 'button.select-box__options-item.--active'
        elements = self.await_elements(driver, 4, method, select)

        return elements, expected_text

    def dropdown_value_marker_displayed(self, element):
        select = 'span.select-box__options-item-active-icon'
        try:
            element.find_element_by_css_selector(select)
            return True
        except [NoSuchElementException, TimeoutException, StaleElementReferenceException]:
            return False

    def dropdown_value_tomorrow(self, driver):
        expected_text = u'Завтра'
        method = By.CSS_SELECTOR
        select = 'button[data-test-id="null.1"]'
        element = self.await_element(driver, 4, method, select)

        return element, expected_text

    def dropdown_button_tomorrow(self, driver):
        expected_text = u'Расписание на завтра'
        method = By.CSS_SELECTOR
        select = 'div[data-test-id="date_filter"]'
        element = self.await_element(driver, 4, method, select)
        element = element.find_element_by_css_selector('span[class=select-box__title]')

        return element, expected_text


    def res_grid(self, driver):
        method = By.ID
        select = 'doctor_list'
        element = self.await_element(driver, 4, method, select)

        return element

    def results(self, driver):
        method = By.CSS_SELECTOR
        expected_lenght = 10

        elements = []
        for i in range(0, 10):
            select = 'div[data-test-id="doctor_list_item.{}"]'.format(i)
            element = self.await_element(driver, 4, method, select)
            elements.append(element)

        return elements, expected_lenght
