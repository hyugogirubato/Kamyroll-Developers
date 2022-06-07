"""
Project: Kamyroll
File: main.py
Date: 2022.06.07
"""

import KamyrollClient


def main():
    email = 'kr_email@gmail.com'
    password = 'kr_password'
    client = KamyrollClient.Client()

    # [---------- Account ----------]
    # client.create_account(email, password)
    # client.login(email, password)
    # client.refresh_token('Wv8MSRVmNwuqMyquygpnCcPRC335HbLefpMpF9aM9o/fmQzzq/n6F9kuFWEV0wk1Gp7z5HJVbDmzipJ6Dn19Bm2yE2rgChr6q69kwj6XvIR9PKBXnBswX78MT+RMrIJqvbmKQYxNgqnomzCxS0a+qGzl4pnYwjHJ9CZCJLb9RrWAbpIGEkIlYcK1Zcxmck09pWxob/ATe9iQfXGu0v7m4ORnzl0o8Ip3omLobX2zsWPM1xMPeIsBG6nxnmHINcRHsUDrVhfKmv/nBn2MUImvZnlqzOlV8IDVe1ziALA/j3pqp1zhxgH/cisRwqM2fcQMagPIusTmWFjXqVY7FXaSYw==')
    # client.refresh_token(refresh_token)

    # [---------- Profile ----------]
    # client.get_avatar()
    # client.set_avatar('sudachi-1.png')
    # client.set_username('hyugogirubato')
    # client.set_audio_language('ja-JP')
    # client.set_subtitle_language('fr-FR')
    # client.set_email(password, 'email@gmail.com')
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
        client.streams(channel_id, '14354', format='srt')

    elif channel_id == 'crunchyroll':
        # client.search(channel_id, 'golden time', locale=locale)
        # client.seasons(channel_id, 'GY5P48XEY', locale='en-US', filter='Demon Slayer: Kimetsu no Yaiba Entertainment District Arc')
        # client.seasons(channel_id, 'GRJ0J828Y', locale='en-US', filter='Kaguya-sama: Love is War -Ultra Romantic-')
        # client.media(channel_id, 'demon-slayer-kimetsu-no-yaiba', locale=locale)
        # client.movies(channel_id, 'G6MG10746', locale=locale)
        # client.streams(channel_id, 'GJWU2520V', type='adaptive_hls', locale=locale, format='vtt', service='reverso')
        client.seasons(channel_id, 'GRMG8ZQZR', locale=locale, filter='ONE PIECE')

        # client.seasons(channel_id, 'GR2P21J9R', locale=locale, filter='High School DxD')
        # client.seasons(channel_id, 'GR2P21J9R', locale=locale, filter='High School BorN')
        # client.seasons(channel_id, 'GR2P21J9R', locale=locale, filter='High School DxD OVA')
        # client.seasons(channel_id, 'GYX02P3MR', locale=locale, filter='Masamune-kun no Revenge OVA')
        # client.seasons(channel_id, 'GYX02P3MR', locale=locale, filter='Masamune-kun no Revenge')
        # client.seasons(channel_id, 'G6W4QKX0R', locale=locale, filter='Tate no Yuusha no Nariagari Season 2')
        # client.seasons(channel_id, 'G6245PG7Y', locale=locale, filter='Ore ga Suki nano wa Imouto dakedo Imouto ja Nai OVA')
        # client.seasons(channel_id, 'G6245PG7Y', locale=locale, filter='Ore ga Suki nano wa Imouto dakedo Imouto ja Nai')
        # client.seasons(channel_id, 'GY5P48XEY', locale=locale, filter='Kimetsu no Yaiba')
        # client.seasons(channel_id, 'GY5P48XEY', locale=locale, filter='Kimetsu no Yaiba: Mugen Ressha-hen')
        # client.seasons(channel_id, 'G6NQ5DWZ6', locale=locale, filter='Baku no Hero Academia 5')

if __name__ == '__main__':
    main()
