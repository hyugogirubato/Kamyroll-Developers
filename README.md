![Kamyroll-Developers](/resources/kamyroll_developers.png?raw=true)  
[![Version](https://img.shields.io/badge/Version-v2022.01.04-green.svg)](https://shields.io/)
## Description
Server synthesizing requests to compatible sites by providing a response in unified JSON format and offering complete information for each available media.

## Supported sites
| Site         | URL                             |
| :----------- | :------------------------------ |
| Crunchyroll  | https://beta.crunchyroll.com    |
| Funimation   | https://www.funimation.com      |
| ADN          | https://animedigitalnetwork.fr  |


## API Reference
### API address
| Protocol        | Method         | URL                                    |
| :-------------- | :------------- | :------------------------------------- |
| HTTPS           | GET            | https://kamyroll-server.herokuapp.com  |

#### Description
Address of the API, it is this one that is used for all available endpoints.


### Get media information

```https
  GET /v1/media
```

| Parameter       | Type       | Description                 |
| :-------------- | :--------- | :-------------------------- |
| `channel_id`    | `string`   | **Required**. Service name  |
| `media_id`      | `string`   | Media ID                    |
| `slug_show`     | `string`   | Show ID                     |
| `slug_episode`  | `string`   | Media ID                    |
| `email`         | `string`   | Account ID                  |
| `password`      | `string`   | Account password            |
| `bypass`        | `boolean`  | Premium bypass              |
| `country`       | `string`   | Country bypass              |

#### Description
Returns all information related to the defined media. The media statement according to the platforms changes. If the bypass is not available or you do not want to use it but still have been to premium videos, you can use your premium account by filling in the information. If some media are not available in your area to get the video streams, used the country bypass.

#### Use of parameters
| Channel ID     | Type        | Parameter                    |
| :------------- | :---------- | :--------------------------- |
| `crunchyroll`  | Episode     | `media_id`                   |
| `crunchyroll`  | Movie       | `media_id`                   |
| `funimation`   | Episode     | `slug_show`, `slug_episode`  |
| `adn`          | Episode     | `media_id`                   |
| `adn`          | Movie       | `media_id`                   |


### Get subtitles

```https
  GET /v1/subtitles
```

| Parameter     | Type      | Description                 |
| :------------ | :-------- | :-------------------------- |
| `channel_id`  | `string`  | **Required**. Service name  |
| `url`         | `string`  | **Required**. Source URL    |

#### Description
For some streaming services such as ADN, subtitles are encrypted and/or not available in a conventional format. This request therefore allows subtitles in a style-compatible format.


### Get server information

```https
  GET /ip
```

#### Description
Display some information about the server such as its IP address or location.


### Get subtitles

```https
  GET /stats
```

| Parameter  | Type       | Description                 |
| :--------- | :--------- | :-------------------------- |
| `token`    | `string`   | **Required**. Access token  |
| `reset`    | `boolean`  | Reset the stats             |

#### Description
View server statistics.

## Services availability
| Code  | Country             | Crunchyroll         | Funimation          | ADN                 |
| :---- | :------------------ | :------------------ | :------------------ | :------------------ |
| `ar`  | Argentina           | :?:                 | :x:                 | :?:                 |
| `at`  | Austria             | :?:                 | :x:                 | :?:                 |
| `au`  | Australia           | :?:                 | :white_check_mark:  | :?:                 |
| `be`  | Belgium             | :?:                 | :x:                 | :?:                 |
| `bg`  | Bulgaria            | :?:                 | :x:                 | :?:                 |
| `br`  | Brazil              | :white_check_mark:  | :white_check_mark:  | :?:                 |
| `ca`  | Canada              | :white_check_mark:  | :white_check_mark:  | :?:                 |
| `ch`  | Switzerland         | :?:                 | :x:                 | :?:                 |
| `cl`  | Chile               | :?:                 | :x:                 | :?:                 |
| `co`  | Colombia            | :?:                 | :x:                 | :?:                 |
| `cz`  | Czech Republic      | :?:                 | :x:                 | :?:                 |
| `de`  | Germany             | :x:                 | :x:                 | :?:                 |
| `dk`  | Denmark             | :?:                 | :x:                 | :?:                 |
| `es`  | Spain               | :white_check_mark:  | :x:                 | :?:                 |
| `fi`  | Finland             | :?:                 | :x:                 | :?:                 |
| `fr`  | France              | :white_check_mark:  | :x:                 | :white_check_mark:  |
| `gb`  | United Kingdom      | :white_check_mark:  | :white_check_mark:  | :?:                 |
| `gr`  | Greece              | :white_check_mark:  | :x:                 | :?:                 |
| `hk`  | Hong Kong           | :?:                 | :x:                 | :?:                 |
| `hr`  | Croatia             | :?:                 | :x:                 | :?:                 |
| `hu`  | Hungary             | :?:                 | :x:                 | :?:                 |
| `id`  | Indonesia           | :?:                 | :x:                 | :?:                 |
| `ie`  | Ireland             | :white_check_mark:  | :white_check_mark:  | :?:                 |
| `il`  | Israel              | :?:                 | :x:                 | :?:                 |
| `in`  | India               | :?:                 | :x:                 | :?:                 |
| `is`  | Iceland             | :?:                 | :x:                 | :?:                 |
| `it`  | Italy               | :?:                 | :x:                 | :?:                 |
| `jp`  | Japan               | :x:                 | :x:                 | :?:                 |
| `kr`  | Korea               | :?:                 | :x:                 | :?:                 |
| `mx`  | Mexico              | :white_check_mark:  | :white_check_mark:  | :?:                 |
| `nl`  | Netherlands         | :?:                 | :x:                 | :?:                 |
| `no`  | Norway              | :?:                 | :x:                 | :?:                 |
| `nz`  | New Zealand         | :white_check_mark:  | :white_check_mark:  | :?:                 |
| `pl`  | Poland              | :?:                 | :x:                 | :?:                 |
| `ro`  | Romania             | :?:                 | :x:                 | :?:                 |
| `ru`  | Russian Federation  | :?:                 | :x:                 | :?:                 |
| `se`  | Sweden              | :?:                 | :x:                 | :?:                 |
| `sg`  | Singapore           | :?:                 | :x:                 | :?:                 |
| `sk`  | Slovakia            | :?:                 | :x:                 | :?:                 |
| `tr`  | Turkey              | :?:                 | :x:                 | :?:                 |
| `uk`  | United Kingdom      | :white_check_mark:  | :white_check_mark:  | :?:                 |
| `us`  | USA                 | :white_check_mark:  | :white_check_mark:  | :x:                 |

#### Description
The region code is the value to use with the country bypass to define the region used to find the content if it is not available. It is generally not necessary to use the country bypass because the server is located in an area where the service catalogues are the most complete.

## Use
| Site         | URL                                                                    | Parameter
| :----------- | :--------------------------------------------------------------------- | :------------------------------------------
| Crunchyroll  | `/watch/G2XU03VQ5/overwhelming-strength-the-straw-hats-come-together`  | `channel_id=crunchyroll&media_id=G2XU03VQ5`
| Funimation   | `/v/one-piece/overwhelming-strength-the-straw-hats-come-together`      | `channel_id=funimation&slug_show=one-piece&slug_episode=overwhelming-strength-the-straw-hats-come-together`
| ADN          | `/video/one-piece/17889-episode-1000-puissance-hors-du-commun-l-equipage-du-chapeau-de-paille-au-complet`  | `channel_id=adn&media_id=17889`


## Availablity
| Channel ID          | Streams type        | Subtitles locale    | Subtitles format
| :------------------ | :------------------ | :------------------ | :------------------
| `crunchyroll`       | `adaptive_hls`      | `ar-SA`, `de-DE`, `en-US`, `es-419`, `es-ES`, `fr-FR`, `it-IT`, `pt-BR`, `pt-PT`, `ru-RU`, `tr-TR`, `ar-ME`  | `ass`
| `funimation`        | `simulcast_adaptive_hls`, `simulcast_mobile_mp4`, `uncut_adaptive_hls`, `uncut_mobile_mp4`  | `en-US` `pt-BR`, `es-419`, `zh-CN`  | `vtt`, `srt`, `dfxp`
| `adn`               | `mobile_hls`, `sd_hls`, `hd_hls`, `fhd_hls`, `adaptive_hls`  | `fr-FR`  | `ass`

## Language code
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

---
*This script was created by the __Nashi Team__.  
Find us on [discord](https://discord.com/invite/g6JzYbh) for more information on projects in development.*
