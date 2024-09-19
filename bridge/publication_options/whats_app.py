from interfaces.publication import IContent


class ContentWhatsApp(IContent):

    def create_content(self):
        return "Контент WhatsApp"
