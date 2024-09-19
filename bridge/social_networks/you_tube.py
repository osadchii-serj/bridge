from interfaces.social_network import ISocialNetwork


class SocialNetworkYouTube(ISocialNetwork):

    def publish(self):
        self.name_network = "Social Network YouTube"
        print(self.name_network)
        print("Публикация:")
        return self.communication_api.create_content()
