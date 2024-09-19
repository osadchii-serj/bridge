from interfaces.social_network import ISocialNetwork


class SocialNetworkTwitter(ISocialNetwork):

    def publish(self):
        self.name_network = "Messenger Twitter"
        print(self.name_network)
        print("Публикация:")
        return self.communication_api.create_content()
