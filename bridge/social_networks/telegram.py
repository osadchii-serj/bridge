from interfaces.social_network import ISocialNetwork


class SocialNetworkTelegram(ISocialNetwork):

    def publish(self):
        self.name_network = "Messenger Telegram"
        print(self.name_network)
        print("Публикация:")
        return self.communication_api.create_content()
