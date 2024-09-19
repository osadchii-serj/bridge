from interfaces.publication import IContent


class ContentFacebook(IContent):

    def create_content(self):
        return "Контент Facebook"
