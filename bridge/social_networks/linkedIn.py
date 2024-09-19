from interfaces.social_network import ISocialNetwork


class SocialNetworkLinkedin(ISocialNetwork):

    def publish(self):
        self.name_network = "Social Network Linkedin"
        print(self.name_network)
        print("Публикация:")
        return self.communication_api.create_content()
