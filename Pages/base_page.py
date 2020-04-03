class BasePage():  #создаем класс
    def __init__(self, browser, url):     #добавляем метод, добавляем конструктор ключевое слово "__init__"
        self.browser = browser
        self.url = url

    def open(self):                    #добавляем метод
        self.browser.get(self.url)