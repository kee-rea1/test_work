# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class Main():

    def vis_element(self, driver, time, method, select):
        WebDriverWait(driver, time).until(ec.visibility_of_element_located((method, select)))

        return driver.find_element(method, select)

    def await_element(self, driver, time, method, select):
        WebDriverWait(driver, time).until(ec.presence_of_element_located((method, select)))

        return driver.find_element(method, select)

    def await_elements(self, driver, time, method, select):
        WebDriverWait(driver, time).until(ec.presence_of_all_elements_located((method, select)))

        return driver.find_elements(method, select)

    def work_with_frame(self, d, element):
        pew = element.find_element_by_tag_name("iframe")
        d.switch_to.frame(pew)
        # try:
        #     pew = d.find_element_by_class_name("html-banner-place")
        # except NoSuchElementException:
        #     pew = d.find_element_by_class_name("html5-banner-place")
        # pew = pew.find_element_by_tag_name("iframe")
        # d.switch_to.frame(pew)
        # pew = d.find_element_by_class_name('TestBanner_outerBlock')

        return pew

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
            self.vis_element(driver, 1, method, select)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def dropdown_value_default_active(self, driver):
        expected_text = u'Все дни'
        method = By.CSS_SELECTOR
        # select = 'span[class="select-box__options-item-title]"]'
        select = 'button.select-box__options-item.--active'
        elements = self.await_elements(driver, 4, method, select)

        return elements, expected_text

    def dropdown_value_marker_displayed(self, element):
        select = 'span.select-box__options-item-active-icon'
        try:
            element.find_element_by_css_selector(select)
            return True
        except [NoSuchElementException, TimeoutException]:
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

        return element, expected_text


    def res_grid(self, driver):
        method = By.ID
        # select = 'div[class="the-doctor-list-items"]'
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