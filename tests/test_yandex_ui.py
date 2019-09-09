from tests.utils.ui import UI


class TestYandexTranslateUI:
    """ Yandex Translate UI test suite. """

    @staticmethod
    def setup():
        """
        Opens 'https://translate.yandex.ru' with chromedriver.
        """
        UI.open_website()

    @staticmethod
    def teardown():
        """
        Close the chromedriver window.
        """
        UI.close_website()

    def test_source_field_works(self):
        """
        Checks, that source field works correct.
        """
        UI.translate_text('s')
        assert UI.read_source_text() == 's'

    def test_en_ru_translation(self):
        """
        Checks correct english-russian translation.
        """
        UI.select_languages('en', 'ru')
        UI.translate_text('cat')
        assert UI.read_translation() == 'кошка'

    def test_ru_en_translation(self):
        """
        Checks correct russian-english translation.
        """
        UI.select_languages('ru', 'en')
        UI.translate_text('кошка')
        assert UI.read_translation() == 'cat'

    def test_language_auto_identification(self):
        """
        Checks correct language auto-identification.
        """
        UI.translate_text('собака')
        assert UI.check_expected_src_language('РУССКИЙ')

    def test_virtual_keyboard(self):
        """
        Checks, that virtual keyboard works.
        """
        UI.select_languages('en', 'ru')
        UI.virtual_keyboard_type_cat()
        assert UI.read_source_text() == 'cat'

