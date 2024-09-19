from interfaces.publication import IContent


class ContentTwitter(IContent):

    def create_content(self):
        return "Контент Twitter"
