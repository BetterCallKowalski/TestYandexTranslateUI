from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class UI:
    """
    Yandex Translate UI tools with Selenium WebDriver.
    """

    driver = WebDriver(executable_path='C://selenium//chromedriver.exe')

    @staticmethod
    def open_website():
        """
        Opens 'https://translate.yandex.ru' with chromedriver.
        """
        UI.driver.get('https://translate.yandex.ru')

    @staticmethod
    def close_website():
        """
        Close the chromedriver window.
        """
        UI.driver.close()

    @staticmethod
    def select_languages(src_lang, dst_lang):
        """
        Selects src_lang to dst_lang translation.
        """
        src_l = src_lang
        dst_l = dst_lang

        x_fr = "//div[@id='srcLangListboxContent']/div[@class='listbox-column']/div[@data-value='{}']".format(src_l)
        x_to = "//div[@id='dstLangListboxContent']/div[@class='listbox-column']/div[@data-value='{}']".format(dst_l)

        UI.driver.find_element_by_id('srcLangButton').click()
        UI.driver.find_element_by_xpath(x_fr).click()

        UI.driver.find_element_by_id('dstLangButton').click()
        UI.driver.find_element_by_xpath(x_to).click()

    @staticmethod
    def translate_text(text):
        """
        Sends text to source field.
        """
        text = text
        UI.driver.find_element_by_id('fakeArea').send_keys(text)

    @staticmethod
    def read_translation():
        """
        Returns translated text.
        """
        translation = WebDriverWait(UI.driver, 3). \
            until(ec.presence_of_element_located((By.XPATH, "//span[@data-complaint-type='fullTextTranslation']/span")))
        return translation.text

    @staticmethod
    def read_source_text():
        """
        Returns source field text.
        """
        source = UI.driver.find_element_by_id('fakeArea')
        return source.text

    @staticmethod
    def check_expected_src_language(expected_language):
        """
        Returns True if source language changed to expected language or returns False if not.
        """
        lang = expected_language
        src_lang = WebDriverWait(UI.driver, 2).\
            until(ec.text_to_be_present_in_element((By.ID, "srcLangButton"), lang))
        return src_lang

    @staticmethod
    def virtual_keyboard_type_cat():
        """
        Types word 'cat' using virtual keyboard.
        """
        UI.driver.find_element_by_id("keyboardButton").click()

        UI.driver.find_element_by_xpath("//div[@data-keycode='67']").click()  # 'c' button
        UI.driver.find_element_by_xpath("//div[@data-keycode='65']").click()  # 'a' button
        UI.driver.find_element_by_xpath("//div[@data-keycode='84']").click()  # 't' button
