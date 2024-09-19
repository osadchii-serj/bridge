from interfaces.social_network import ISocialNetwork


class SocialNetworkInstagram(ISocialNetwork):

    def publish(self):
        self.name_network = "Social Network Instagram"
        print(self.name_network)
        print("Публикация:")
        return self.communication_api.create_content()
