from interfaces.publication import IContent


class ContentLinkedin(IContent):

    def create_content(self):
        return "Контент Linkedin"
