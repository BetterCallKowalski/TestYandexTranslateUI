from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class YUI:
    """
    Yandex Translate UI tools with Selenium WebDriver.
    """

    def __init__(self, chromedriver_path):
        chromedriver_path = chromedriver_path
        self.driver = WebDriver(executable_path=chromedriver_path)

    def open_website(self, url):
        """
        Opens 'https://translate.yandex.ru' with chromedriver.
        """
        yatr_url = url
        self.driver.get(yatr_url)

    def close_website(self):
        """
        Close the chromedriver window.
        """
        self.driver.close()

    def select_languages(self, src_lang, dst_lang):
        """
        Selects src_lang to dst_lang translation.
        """
        src_l = src_lang
        dst_l = dst_lang

        x_fr = "//div[@id='srcLangListboxContent']/div[@class='listbox-column']/div[@data-value='{}']".format(src_l)
        x_to = "//div[@id='dstLangListboxContent']/div[@class='listbox-column']/div[@data-value='{}']".format(dst_l)

        self.driver.find_element_by_id('srcLangButton').click()
        self.driver.find_element_by_xpath(x_fr).click()

        self.driver.find_element_by_id('dstLangButton').click()
        self.driver.find_element_by_xpath(x_to).click()

    def translate_text(self, text):
        """
        Sends text to source field.
        """
        text = text
        self.driver.find_element_by_id('fakeArea').send_keys(text)

    def read_translation(self):
        """
        Returns translated text.
        """
        translation = WebDriverWait(self.driver, 3). \
            until(ec.presence_of_element_located((By.XPATH, "//span[@data-complaint-type='fullTextTranslation']/span")))
        return translation.text

    def read_source_text(self):
        """
        Returns source field text.
        """
        source = self.driver.find_element_by_id('fakeArea')
        return source.text

    def press_clear_button(self):
        """
        Returns source field text.
        """
        self.driver.find_element_by_id('clearButton').click()

    def check_expected_src_language(self, expected_language):
        """
        Returns True if source language changed to expected language or returns False if not.
        """
        lang = expected_language
        src_lang = WebDriverWait(self.driver, 2).\
            until(ec.text_to_be_present_in_element((By.ID, "srcLangButton"), lang))
        return src_lang

    def type_with_virtual_keyboard(self, string):
        """
        Types word 'cat' using virtual keyboard.
        """
        string = string
        assert len(string) != 0
        assert type(string) == str

        self.driver.find_element_by_id("keyboardButton").click()

        for char in string:
            keyboard_button_xpath = "//div[@data-keycode='" + str(ord(char)) + "']"
            self.driver.find_element_by_xpath(keyboard_button_xpath).click()
