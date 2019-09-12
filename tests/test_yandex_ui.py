import yaml
from tests.yui.yui import YUI


class TestYandexTranslateUI:
    """ Yandex Translate UI test suite. """

    def setup(self):
        """
        Opens 'https://translate.yandex.ru' with chromedriver.
        """
        config = yaml.safe_load(open('config.yml', encoding='utf-8'))  # Loading config from 'config.yml'

        self.yui = YUI(config['chromedriver_path'])
        self.yui.open_website(config['yatr_url'])

    def teardown(self):
        """
        Close the chromedriver window.
        """
        self.yui.close_website()

    def test_en_ru_translation(self):
        """
        Checks correct english-russian translation.
        """

        self.yui.select_languages('en', 'ru')
        self.yui.translate_text('cat')
        assert self.yui.read_translation() == 'кошка'

    def test_ru_en_translation(self):
        """
        Checks correct russian-english translation.
        """
        self.yui.select_languages('ru', 'en')
        self.yui.translate_text('кошка')
        assert self.yui.read_translation() == 'cat'

    def test_russian_language_auto_identification(self):
        """
        Checks correct russian language auto-identification.
        """
        self.yui.translate_text('собака')
        assert self.yui.check_expected_src_language('РУССКИЙ')

    def test_english_language_auto_identification(self):
        """
        Checks correct english language auto-identification.
        """
        self.yui.translate_text('dog')
        assert self.yui.check_expected_src_language('АНГЛИЙСКИЙ')

    def test_clear_button(self):
        """
        Checks, that clear button works.
        """
        self.yui.translate_text("mouse")
        self.yui.press_clear_button()

        assert self.yui.read_source_text() == ""

    def test_virtual_keyboard(self):
        """
        Checks, that virtual keyboard works.
        """
        self.yui.type_with_virtual_keyboard("A")
        assert self.yui.read_source_text() == 'a'
