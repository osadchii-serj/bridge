from interfaces.publication import IContent


class ContentInstagram(IContent):

    def create_content(self):
        return "Контент Instagram"
