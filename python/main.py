"""
Project: Kamyroll
File: main.py
Date: 2022.05.04
"""

import KamyrollClient


def main():
    email = 'kr_email'
    password = 'kr_password'
    client = KamyrollClient.Client()

    # [---------- Account ----------]
    # client.create_account(email, password)
    client.login(email, password)
    # client.refresh_token(refresh_token)

    # [---------- Profile ----------]
    # client.get_avatar()
    # client.set_avatar('sudachi-1.png')
    # client.set_username('hyugogirubato')
    # client.set_audio_language('ja-JP')
    # client.set_subtitle_language('fr-FR')
    # client.set_email(password, 'hyugogirubato@gmail.com')
    # client.set_password(password, 'password')
    # client.delete_account(password)
    # client.add_subscription(password, 'crunchyroll', 'cr_email', 'cr_password')
    # client.add_subscription(password, 'animedigitalnetwork', 'adn_email', 'adn_password')
    # client.remove_subscription(password, 'animedigitalnetwork')
    # client.subscription()
    # client.profile()

    # [---------- Server ----------]
    # client.configuration()
    # client.channels()
    # client.ip()       # Reserved
    # client.database() # Reserved

    # [---------- Anime ----------]
    channel_id = 'crunchyroll'
    locale = 'fr-FR'

    if channel_id == 'animedigitalnetwork':
        # EPISODE: 14354
        # SERIES: 712
        # MOVIE: 9813
        # MOVIE_LISTING: 556
        # client.search(channel_id, 'blea')
        # client.seasons(channel_id, '712')
        # client.media(channel_id, '361')
        # client.movies(channel_id, '361')
        client.streams(channel_id, '14354')

    elif channel_id == 'crunchyroll':
        # client.search(channel_id, 'Mizo', locale=locale)
        # client.seasons(channel_id, 'GQWH0M455', locale=locale)
        # client.media(channel_id, 'G62PEZ2E6', locale=locale)
        # client.movies(channel_id, 'G6MG10746', locale=locale)
        client.streams(channel_id, 'GZ7UVX45W', type='adaptive_hls', locale=locale)


if __name__ == '__main__':
    main()
