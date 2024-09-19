from social_networks.whats_app import SocialNetworkWhatsApp
from social_networks.instagram import SocialNetworkInstagram
from social_networks.facebook import SocialNetworkFacebook
from social_networks.telegram import SocialNetworkTelegram
from social_networks.you_tube import SocialNetworkYouTube
from social_networks.linkedIn import SocialNetworkLinkedin
from social_networks.twitter import SocialNetworkTwitter
from social_networks.tik_tok import SocialNetworkTikTok

from publication_options.whats_app import ContentWhatsApp
from publication_options.instagram import ContentInstagram
from publication_options.facebook import ContentFacebook
from publication_options.telegram import ContentTelegram
from publication_options.you_tube import ContentYouTube
from publication_options.linkedIn import ContentLinkedin
from publication_options.twitter import ContentTwitter
from publication_options.tik_tok import ContentTikTok

from interfaces.social_network import ISocialNetwork

from random import choice


def client_code(social_network: ISocialNetwork):
    print(social_network.publish())


if __name__ == "__main__":

    list_of_social_networks = [
        SocialNetworkWhatsApp,
        SocialNetworkInstagram,
        SocialNetworkFacebook,
        SocialNetworkTelegram,
        SocialNetworkYouTube,
        SocialNetworkLinkedin,
        SocialNetworkTwitter,
        SocialNetworkTikTok,
    ]

    list_of_content = [
        ContentWhatsApp(),
        ContentInstagram(),
        ContentFacebook(),
        ContentTelegram(),
        ContentYouTube(),
        ContentLinkedin(),
        ContentTwitter(),
        ContentTikTok(),
    ]

    for _ in range(10):

        network = choice(list_of_social_networks)
        content = choice(list_of_content)

        client_code(network(content))
        print()
