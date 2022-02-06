![Kamyroll-Developers](/resources/kamyroll_developers.png?raw=true)  
[![Version](https://img.shields.io/badge/Version-v2022.02.06-green.svg)](https://shields.io/)
## Description
Server synthesizing requests to compatible sites by providing a response in unified JSON format and offering complete information for each available media.

## API address
| Protocol        | Method         | URL                                    |
| :-------------- | :------------- | :------------------------------------- |
| HTTPS           | GET            | https://kamyroll-server.herokuapp.com  |

## Supported sites
<details><summary>ADN</summary>

Website: https://animedigitalnetwork.fr

## Parent
```https
  GET /v1/parent
```
| Parameter     | Type       | Description                      |
| :------------ | :--------- | :------------------------------- |
| `channel_id`  | `string`   | **Required**. Service name       |
| `slug_title`  | `string`   | **Required**. Parent slug title  |

## Streams
```https
  GET /v1/streams
```
| Parameter     | Type       | Description                    |
| :------------ | :--------- | :----------------------------- |
| `channel_id`  | `string`   | **Required**. Service name     |
| `id`          | `string`   | **Required**. Episode ID       |

## Supported type
| Type          | Parent              | Streams             |
| :------------ | :------------------ | :------------------ |
| Series        | :white_check_mark:  | :x:                 |
| Episode       | :x:                 | :white_check_mark:  |
| OAV           | :white_check_mark:  | :white_check_mark:  |
| Feature film  | :white_check_mark:  | :white_check_mark:  |
| Short film    | :white_check_mark:  | :white_check_mark:  |

## Use
| URL           | `/video/one-piece/17889-episode-1000-puissance-hors-du-commun-l-equipage-du-chapeau-de-paille-au-complet`  |
| :------------ | :--------------------------------------------------------------------------------------------------------- |
| `channel_id`  | `adn`                                                                                                      |
| `slug_title`  | `one-piece`                                                                                                |
| `id`          | `17889`                                                                                                    |

## Availablity
| Type              | Availablity                  |
| :---------------- | :--------------------------- |
| Streams type      | `adaptive_hls`               |
| Subtitles locale  | `fr-FR`                      |
| Subtitles format  | `ass`                        |
| Resolutions       | `360`, `480`, `720`, `1080`  |

</details>

<details><summary>Crunchyroll</summary>

Website: https://beta.crunchyroll.com

## Parent
```https
  GET /v1/parent
```
| Parameter     | Type       | Description                 |
| :------------ | :--------- | :-------------------------- |
| `channel_id`  | `string`   | **Required**. Service name  |
| `id`          | `string`   | **Required**. Parent ID     |
| `locale`      | `string`   | Language code               |

## Streams
```https
  GET /v1/streams
```
| Parameter     | Type       | Description                 |
| :------------ | :--------- | :-------------------------- |
| `channel_id`  | `string`   | **Required**. Service name  |
| `id`          | `string`   | **Required**. Episode ID    |
| `locale`      | `string`   | Language code               |

## Supported type
| Type           | Parent              | Streams             |
| :------------- | :------------------ | :------------------ |
| Series         | :white_check_mark:  | :x:                 |
| Episode        | :x:                 | :white_check_mark:  |
| Movie listing  | :white_check_mark:  | :x:                 |
| Movie          | :x:                 | :white_check_mark:  |

## Use
| URL           | `/watch/G2XU03VQ5/overwhelming-strength-the-straw-hats-come-together`  |
| :------------ | :--------------------------------------------------------------------- |
| `channel_id`  | `crunchyroll`                                                          |
| `id`          | `G2XU03VQ5`                                                            |

## Availablity
| Type              | Availablity                                                                                                  |
| :---------------- | :----------------------------------------------------------------------------------------------------------- |
| Streams type      | `adaptive_hls`                                                                                               |
| Subtitles locale  | `ar-SA`, `de-DE`, `en-US`, `es-419`, `es-ES`, `fr-FR`, `it-IT`, `pt-BR`, `pt-PT`, `ru-RU`, `tr-TR`, `ar-ME`  |
| Subtitles format  | `ass`                                                                                                        |
| Resolutions       | `80`, `96`, `240`, `360`, `480`, `720`, `1080`                                                                     |

</details>

<details><summary>Funimation</summary>

website:  https://www.funimation.com

## Parent
```https
  GET /v1/parent
```
| Parameter     | Type       | Description                      |
| :------------ | :--------- | :------------------------------- |
| `channel_id`  | `string`   | **Required**. Service name       |
| `slug_title`  | `string`   | **Required**. Parent slug title  |

## Streams
```https
  GET /v1/streams
```
| Parameter       | Type       | Description                      |
| :-------------- | :--------- | :------------------------------- |
| `channel_id`    | `string`   | **Required**. Service name       |
| `slug_title`    | `string`   | **Required**. Parent slug title  |
| `slug_episode`  | `string`   | **Required**. Slug episode       |

## Supported type
| Type           | Parent              | Streams             |
| :------------- | :------------------ | :------------------ |
| Series         | :white_check_mark:  | :x:                 |
| Episode        | :white_check_mark:  | :white_check_mark:  |
| Trailer        | :white_check_mark:  | :white_check_mark:  |
| Movie          | :white_check_mark:  | :white_check_mark:  |

## Use
| URL             | `/v/fairy-tail/natsu-vs-yuka-the-wave-user`  |
| :-------------- | :------------------------------------------- |
| `channel_id`    | `funimation`                                 |
| `slug_title`    | `fairy-tail`                                 |
| `slug_episode`  | `natsu-vs-yuka-the-wave-user`                |

## Availablity
| Type              | Availablity                                                                                 |
| :---------------- | :------------------------------------------------------------------------------------------ |
| Streams type      | `simulcast_adaptive_hls`, `simulcast_mobile_mp4`, `uncut_adaptive_hls`, `uncut_mobile_mp4`  |
| Subtitles locale  | `en-US` `pt-BR`, `es-419`, `zh-CN`                                                          |
| Subtitles format  | `ass`                                                                                       |
| Resolutions       | `234`, `360`, `432`, `540`, `720`, `1080`                                                   |

</details>

## Additional options
<details><summary>Login</summary>

Allows you to log in to use your subscription to unlock content.

| Parameter   | Type       | Description  |
| :---------- | :--------- | :----------- |
| `email`     | `string`   | Email        |
| `password`  | `string`   | Password     |

## Supported sites
| Type         | Supported           |
| :----------- | :------------------ |
| ADN          | :white_check_mark:  |
| Crunchyroll  | :white_check_mark:  |
| Funimation   | :white_check_mark:  |

</details>

<details><summary>Bypass</summary>

Allows you to get premium content without needing a subscription.

| Parameter   | Type       | Description  |
| :---------- | :--------- | :----------- |
| `bypass`    | `boolean`  | Activate     |

## Supported sites
| Type         | Supported           |
| :----------- | :------------------ |
| ADN          | :white_check_mark:  |
| Crunchyroll  | :white_check_mark:  |
| Funimation   | :white_check_mark:  |

</details>

<details><summary>API error</summary>

Form of an api error.

````json
{"error": true, "code": "bad_auth_params", "message": "Unauthenticated request."}
````
## Errors list
| Code                        | Message                                                          |
| :-------------------------- | :--------------------------------------------------------------- |
| `bad_identifiers`           | `The identification information is invalid.`                     |
| `bad_bypass`                | `Bypass service is unavailable.`                                 |
| `bad_service`               | `The service is unavailable.`                                    |
| `bad_bypass_declaration`    | `Bypass declaration error.`                                      |
| `bad_password_entry`        | `Password is not defined.`                                       |
| `bad_email_entry`           | `Email is not defined.`                                          |
| `bad_bypass_definition`     | `The bypass cannot be activated with the use of an identifier.`  |
| `bad_country`               | `Country is not available or does not exist.`                    |
| `bad_initialize`            | `Service initialization error.`                                  |
| `bad_service_country`       | `The service is not available in this country.`                  |
| `bad_locale`                | `This locale does not exist.`                                    |
| `unknown_id`                | `Id was not recognized.`                                         |
| `missing_id`                | `Id is undefined.`                                               |
| `unknown_type`              | `The type is not recognized.`                                    |
| `bad_id_type`               | `The defined id is not compatible.`                              |
| `premium_only`              | `Video requires premium access.`                                 |
| `bad_playback`              | `An error occurred while loading the playbacks.`                 |
| `bad_href`                  | `Unable to load href.`                                           |
| `bad_show_id`               | `Unable to load show id.`                                        |
| `bad_slug_title`            | `Unable to load slug title.`                                     |
| `bad_episode_extract`       | `Error extracting episode.`                                      |
| `bad_movie_extract`         | `Error extracting movie.`                                        |
| `bad_series_extract`        | `Error extracting series.`                                       |
| `missing_channel_id`        | `Channel id is undefined.`                                       |
| `missing_slug_title`        | `Slug title is undefined.`                                       |
| `missing_slug_episode`      | `Slug episode is undefined.`                                     |
| `unknown_channel_id`        | `Channel id was not recognized.`                                 |
| `unknown_extractor`         | `Unable to set extractor.`                                       |
| `bad_player_initialize`     | `A player initialization error has occurred.`                    |
| `bad_player_connection`     | `Unable to connect to the player. Try again.`                    |
| `unknown_error`             | `An unknown error has occurred.`                                 |
| `bad_videos`                | `Unable to find the video associated with the id.`               |
| `missing_json`              | `Json is undefined.`                                             |
| `bad_json`                  | `Json data is invalid.`                                          |
| `unsupported_channel`       | `The channel is not supported.`                                  |
| `bad_subtitles`             | `An error occurred while creating the subtitles.`                |
| `bad_auth_params`           | `Unauthenticated request.`                                       |
| `mature_content`            | `You need to enable mature content.`                             |
| `bad_proxy_initialization`  | `An error occurred while creating the proxy.`                    |
| `bad_proxy_identification`  | `An error occurred during proxy authentication.`                 |
| `bad_ip_loading`            | `An error occurred while loading the IP.`                        |
| `missing_token`             | `Token is undefined.`                                            |
| `bad_token`                 | `The access token is invalid.`                                   |
| `bad_reset`                 | `An error occurred while resetting.`                             |
| `drm_restrictions`          | `The video is blocked by a DRM.`                                 |

</details>

<details><summary>Management</summary>

## IP

Displays server information.

```https
  GET /ip
```

## Config

Display the current server status with the list of available services.

```https
  GET /v2/config
```

## Stats

Shows how often the server is used.

```https
  GET /stats
```
| Parameter  | Type       | Description                 |
| :--------- | :--------- | :-------------------------- |
| `token`    | `string`   | **Required**. Access token  |
| `reset`    | `boolean`  | Reset                       |

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

All the information sent used with the API, whether it is the services used, identification information or even the targeted media are not saved.

</details>

<details><summary>Support</summary>

If you like the service, you have several possibilities to help us by contacting us on our discord server.
To support us, you can:
- Donate money to ensure bypass longevity and developer support
- Share your premium account credentials for use as a bypass
- Talk about us to developers or communities

</details>


---
*This script was created by the __Nashi Team__.  
Find us on [discord](https://discord.com/invite/g6JzYbh) for more information on projects in development.*
