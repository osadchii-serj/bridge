from interfaces.publication import IContent


class ContentYouTube(IContent):

    def create_content(self):
        return "Контент YouTube"
