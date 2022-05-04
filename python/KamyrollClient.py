"""
Project: Kamyroll
File: KamyrollClient.py
Date: 2022.05.04
"""

import json
import sys
import pyperclip
import requests

BASE_API = 'https://api.kamyroll.tech'
USER_AGENT = 'Kamyroll/3.17.0 Android/7.1.2 okhttp/4.9.1'
HEADERS = {
    'user-agent': USER_AGENT,
    'authorization': 'Basic BCoB9f4m4lSlo+fp05PjlwWcplxQXDT+N+1FfvsyoF41YSy8nH+kuJBQowYrVkiZq6PvTvjFEoQQvzJOt3pJZA=='
}

""" ENDPOINTS
/auth/v1/token
/accounts/v1/me/profile
/accounts/v1/me/credentials
/accounts/v1/me/profile
/accounts/v2
/subs/v1/subscriptions
/content/v1/search
/content/v1/seasons
/content/v1/media
/content/v1/movies
/assets/v1/avatar
/videos/v1/streams
/builder/v1/m3u8
/builder/v1/subtitles
/index/v1/channels
/index/v1/config
/index/v2/ip
/index/v2/database
"""


def _check_request(response):
    if not response.ok:
        print(response.status_code)
        print(response.text)
        sys.exit(1)
    return response.json()


def _copy(response):
    print(response)
    pyperclip.copy(json.dumps(response))


class Client:

    def __init__(self):
        self._headers = {}

    def create_account(self, email, password):
        data = {'email': email, 'password': password}
        response = _check_request(requests.post(f'{BASE_API}/accounts/v2', data=data, headers=HEADERS))
        self._headers = {
            'user-agent': USER_AGENT,
            'authorization': f"{response['token_type']} {response['access_token']}"
        }

    def login(self, email, password):
        data = {
            'email': email,
            'password': password,
            'grant_type': 'password',
            'scope': 'offline_access'
        }
        response = _check_request(requests.post(f'{BASE_API}/auth/v1/token', data=data, headers=HEADERS))
        self._headers = {
            'user-agent': USER_AGENT,
            'authorization': f"{response['token_type']} {response['access_token']}"
        }

    def refresh_token(self, refresh_token):
        data = {
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token',
            'scope': 'offline_access'
        }
        response = _check_request(requests.post(f'{BASE_API}/auth/v1/token', data=data, headers=HEADERS))
        self._headers = {
            'user-agent': USER_AGENT,
            'authorization': f"{response['token_type']} {response['access_token']}"
        }

    def get_avatar(self):
        _copy(_check_request(requests.get(f'{BASE_API}/assets/v1/avatar', headers=self._headers)))

    def set_avatar(self, avatar):
        _check_request(requests.put(f'{BASE_API}/accounts/v1/me/profile', data={'avatar': avatar}, headers=self._headers))

    def set_username(self, username):
        _check_request(requests.put(f'{BASE_API}/accounts/v1/me/profile', data={'username': username}, headers=self._headers))

    def set_audio_language(self, language):
        _check_request(requests.put(f'{BASE_API}/accounts/v1/me/profile', data={'preferred_audio_language': language}, headers=self._headers))

    def set_subtitle_language(self, language):
        _check_request(requests.put(f'{BASE_API}/accounts/v1/me/profile', data={'preferred_subtitle_language': language}, headers=self._headers))

    def set_email(self, current_password, new_email):
        data = {
            'current_password': current_password,
            'email': new_email
        }
        _check_request(requests.put(f'{BASE_API}/accounts/v1/me/credentials', data=data, headers=self._headers))

    def set_password(self, current_password, new_password):
        data = {
            'current_password': current_password,
            'password': new_password
        }
        _check_request(requests.put(f'{BASE_API}/accounts/v1/me/credentials', data=data, headers=self._headers))

    def delete_account(self, current_password):
        data = {
            'current_password': current_password,
            'scope': 'delete_profile'
        }
        _check_request(requests.put(f'{BASE_API}/accounts/v1/me/credentials', data=data, headers=self._headers))

    def add_subscription(self, current_password, channel_id, email, password):
        data = {
            'current_password': current_password,
            'channel_id': channel_id,
            'email': email,
            'password': password,
            'scope': 'add_channel'
        }
        _check_request(requests.put(f'{BASE_API}/accounts/v1/me/credentials', data=data, headers=self._headers))

    def remove_subscription(self, current_password, channel_id):
        data = {
            'current_password': current_password,
            'channel_id': channel_id,
            'scope': 'remove_channel'
        }
        _check_request(requests.put(f'{BASE_API}/accounts/v1/me/credentials', data=data, headers=self._headers))

    def subscription(self):
        _copy(_check_request(requests.get(f'{BASE_API}/subs/v1/subscriptions', headers=self._headers)))

    def profile(self):
        _copy(_check_request(requests.get(f'{BASE_API}/accounts/v1/me/profile', headers=self._headers)))

    def search(self, channel_id, query, limit=100, locale='en-US'):
        params = {
            'channel_id': channel_id,
            'query': query,
            'limit': limit,
            'locale': locale
        }
        _copy(_check_request(requests.get(f'{BASE_API}/content/v1/search', params=params, headers=self._headers)))

    def seasons(self, channel_id, show_id, locale='en-US'):
        params = {
            'channel_id': channel_id,
            'id': show_id,
            'locale': locale
        }
        _copy(_check_request(requests.get(f'{BASE_API}/content/v1/seasons', params=params, headers=self._headers)))

    def movies(self, channel_id, movie_id, locale='en-US'):
        params = {
            'channel_id': channel_id,
            'id': movie_id,
            'locale': locale
        }
        _copy(_check_request(requests.get(f'{BASE_API}/content/v1/movies', params=params, headers=self._headers)))

    def media(self, channel_id, media_id, locale='en-US'):
        params = {
            'channel_id': channel_id,
            'id': media_id,
            'locale': locale
        }
        _copy(_check_request(requests.get(f'{BASE_API}/content/v1/media', params=params, headers=self._headers)))

    def streams(self, channel_id, media_id, type='adaptive_hls', locale='en-US', ):
        params = {
            'channel_id': channel_id,
            'id': media_id,
            'locale': locale,
            'type': type
        }
        _copy(_check_request(requests.get(f'{BASE_API}/videos/v1/streams', params=params, headers=self._headers)))

    def channels(self):
        _copy(_check_request(requests.get(f'{BASE_API}/index/v1/channels', headers=self._headers)))

    def configuration(self):
        _copy(_check_request(requests.get(f'{BASE_API}/index/v1/config', headers=self._headers)))

    def ip(self):
        _copy(_check_request(requests.get(f'{BASE_API}/index/v2/ip', headers=self._headers)))

    def database(self):
        _copy(_check_request(requests.get(f'{BASE_API}/index/v2/database', headers=self._headers)))
