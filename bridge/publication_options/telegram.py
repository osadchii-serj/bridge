from interfaces.publication import IContent


class ContentTelegram(IContent):

    def create_content(self):
        return "Контент Telegram"
