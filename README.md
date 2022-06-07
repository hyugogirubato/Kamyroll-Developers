![Kamyroll-Developers](/resource/kamyroll_developers.png?raw=true)  
[![Version](https://img.shields.io/badge/Version-v3.17.0-green.svg)](https://shields.io/)
## Description
Server synthesizing requests to compatible sites by providing a response in unified JSON format and offering complete information for each available media.

## Use
A python client is available so that you can use the API more easily. You will find in it the global use of the API in order to allow you an optimal use of it. Python script [here](/python/main.py).


## API
<details><summary>Authentication</summary>

````yml
BASE_URL: 'https://kamyroll.herokuapp.com'
USER_AGENT: Kamyroll/3.18.0 Android/7.1.2 okhttp/4.9.1  
BASIC_AUTHORIZATION: Basic vrvluizpdr2eby+RjSKM17dOLacExxq1HAERdxQDO6+2pHvFHTKKnByPD7b6kZVe1dJXifb6SG5NWMz49ABgJA==  
````
</details>


### Account
<details><summary>Create account</summary>

Request
```https
  POST /accounts/v2
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BASIC_AUTHORIZATION"
}
````
Body
````json
{
  "email": "EMAIL",
  "password": "PASSWORD"
}
````
</details>

<details><summary>Login (credentials)</summary>

Request
```https
  POST /auth/v1/token
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BASIC_AUTHORIZATION"
}
````
Body
````json
{
  "email": "EMAIL",
  "password": "PASSWORD",
  "grant_type": "password",
  "scope": "offline_access"
}
````
</details>

<details><summary>Login (Refresh token)</summary>

Request
```https
  POST /auth/v1/token
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BASIC_AUTHORIZATION"
}
````
Body
````json
{
  "refresh_token": "REFRESH_TOKEN",
  "grant_type": "refresh_token",
  "scope": "offline_access"
}
````
</details>


### Profile
<details><summary>List avatars</summary>

Request
```https
  GET /assets/v1/avatar
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
</details>

<details><summary>Set avatar</summary>

Request
```https
  PUT /accounts/v1/me/profile
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Body
````json
{
  "avatar": "AVATAR"
}
````
</details>

<details><summary>Set username</summary>

Request
```https
  PUT /accounts/v1/me/profile
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Body
````json
{
  "username": "USERNAME"
}
````
</details>

<details><summary>Set audio language</summary>

Request
```https
  PUT /accounts/v1/me/profile
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Body
````json
{
  "preferred_audio_language": "LOCALE"
}
````
</details>

<details><summary>Set subtitle language</summary>

Request
```https
  PUT /accounts/v1/me/profile
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Body
````json
{
  "preferred_subtitle_language": "LOCALE"
}
````
</details>

<details><summary>Set email</summary>

Request
```https
  PUT /accounts/v1/me/credentials
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Body
````json
{
  "current_password": "PASSWORD",
  "email": "EMAIL"
}
````
</details>

<details><summary>Set password</summary>

Request
```https
  PUT /accounts/v1/me/credentials
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Body
````json
{
  "current_password": "PASSWORD",
  "password": "PASSWORD"
}
````
</details>

<details><summary>Delete account</summary>

Request
```https
  PUT /accounts/v1/me/credentials
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Body
````json
{
  "current_password": "PASSWORD",
  "scope": "delete_profile"
}
````
</details>

<details><summary>Add subscription</summary>

Request
```https
  PUT /accounts/v1/me/credentials
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Body
````json
{
  "current_password": "PASSWORD",
  "channel_id": "CHANNEL_ID",
  "email": "EMAIL",
  "password": "PASSWORD",
  "scope": "add_channel"
}
````
</details>

<details><summary>Remove subscription</summary>

Request
```https
  PUT /accounts/v1/me/credentials
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Body
````json
{
  "current_password": "PASSWORD",
  "channel_id": "CHANNEL_ID",
  "scope": "remove_channel"
}
````
</details>

<details><summary>List subscriptions</summary>

Request
```https
  GET /subs/v1/subscriptions
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
</details>

<details><summary>Profile</summary>

Request
```https
  GET /accounts/v1/me/profile
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
</details>


### Anime
<details><summary>Search</summary>

Request
```https
  GET /content/v1/search
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Queries
````json
{
  "channel_id": "CHANNEL_ID",
  "query": "QUERY",
  "limit": "LIMIT",
  "locale": "LOCALE"
}
````
</details>

<details><summary>Episodes list (series)</summary>

Request
```https
  GET /content/v1/seasons
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Queries
````json
{
  "channel_id": "CHANNEL_ID",
  "id": "SERIES_ID",
  "locale": "LOCALE"
}
````
</details>

<details><summary>Episodes list (movie)</summary>

Request
```https
  GET /content/v1/movies
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Queries
````json
{
  "channel_id": "CHANNEL_ID",
  "id": "MOVIE_ID",
  "locale": "LOCALE"
}
````
</details>

<details><summary>Media info</summary>

Request
```https
  GET /content/v1/media
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Queries
````json
{
  "channel_id": "CHANNEL_ID",
  "id": "MEDIA_ID",
  "locale": "LOCALE"
}
````
</details>

<details><summary>Episode/Movie streams</summary>

Request
```https
  GET /videos/v1/streams
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
Queries
````json
{
  "channel_id": "CHANNEL_ID",
  "id": "MEDIA_ID",
  "locale": "LOCALE",
  "type": "TYPE"
}
````
</details>


## Configuration
<details><summary>Channels</summary>

Request
```https
  GET /index/v1/channels
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
</details>

<details><summary>Configuration</summary>

Request
```https
  GET /index/v1/config
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
</details>

<details><summary>IP</summary>

Request
```https
  GET /index/v2/ip
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
</details>

<details><summary>Database</summary>

Request
```https
  GET /index/v2/database
```
Headers
````json
{
  "user-agent": "USER_AGENT",
  "authorization": "BEARER_AUTHORIZATION"
}
````
</details>


## Informations
<details><summary>Language code</summary>

| Code      | Language               |
| :-------- | :--------------------- |
| `ar-SA`   | Arabic (Saudi Arabia)  |
| `de-DE`   | German                 |
| `en-US`   | English (USA)          |
| `es-419`  | Spanish                |
| `es-ES`   | Spanish (Spain)        |
| `fr-FR`   | French (France)        |
| `it-IT`   | Italian                |
| `pt-BR`   | Portuguese (Brazil)    |
| `pt-PT`   | Portuguese (Portugal)  |
| `ru-RU`   | Russian                |
| `zh-CN`   | Chinese                |
| `tr-TR`   | Turkish                |
| `ar-ME`   | Arabic (Montenegro)    |
| `ja-JP`   | Japanese               |
| ``        | Off                    |

</details>

<details><summary>Bypass</summary>

## Working
The bypass consists of being able to unlock access to videos reserved for paying subscribers on the various price-based services. However, this is not a bug or a fault of the sites. The bypass works using real paid accounts that allow you to generate streaming links thanks to them. This service is offered for free although it is a real cost, that's why not all platforms are supported or the bypass may be unavailable for some of them.

## Identification
The bypass is associated with accounts internal to the script, it does not use credentials data from other API users. Bypass credentials are not disclosed in any way and may be removed at the donor's request if desired.
</details>

<details><summary>Personal data</summary>

Adding a subscription to a service in order to use your personal account if desired requires saving credentials on the API. However, this information is protected (RSA encrypted) and can only be used through your kamyroll account. Once saved, it is possible to withdraw and modify them but not to obtain them in order to ensure the integrity of the data.
</details>

<details><summary>Support</summary>

If you like the service, you have several possibilities to help us by contacting us on our discord server.
To support us, you can:
- Donate money to ensure bypass longevity and developer support
- Share your premium account credentials for use as a bypass
- Talk about us to developers or communities
</details>


---
*This script was created by the __Kamyroll Team__.  
Find us on [discord](https://discord.com/invite/g6JzYbh) for more information on projects in development.*
