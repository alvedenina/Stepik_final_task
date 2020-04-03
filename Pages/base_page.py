from selenium.common.exceptions import NoSuchElementException

class BasePage():  #создаем класс
    def __init__(self, browser, url):     #добавляем метод, добавляем конструктор ключевое слово "__init__"
        self.browser = browser
        self.url = url

    def open(self):                    #добавляем метод
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True