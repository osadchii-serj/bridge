from interfaces.social_network import ISocialNetwork


class SocialNetworkWhatsApp(ISocialNetwork):

    def publish(self):
        self.name_network = "Messenger WhatsApp"
        print(self.name_network)
        print("Публикация:")
        return self.communication_api.create_content()
