# political_arena


[![Maintainability](https://api.codeclimate.com/v1/badges/930de259caf8289c8cc0/maintainability)](https://codeclimate.com/github/kamaathedj/political_arena/maintainability)


[![Build Status](https://travis-ci.org/kamaathedj/political_arena.svg?branch=Development)](https://travis-ci.org/kamaathedj/political_arena)

[![Coverage Status](https://coveralls.io/repos/github/kamaathedj/political_arena/badge.svg?branch=Development)](https://coveralls.io/github/kamaathedj/political_arena?branch=Development)


## Description
Politico enables citizens give their mandate to politicians running for different government offices
while building trust in the process through transparency.
## API Endpoints V1


| **METHODS** | **LINKS** | **DESCRIPTION** |
| --- | --- | --- |
| **POST** | `/api/v1/parties` | Create political party |
| **GET** | `/api/v1/getparties` | Get political party |
| **GET** | `/api/v1/specificparties/<party_id>` | Get specific political party |
| **PATCH** | `/api/v1/getparty/<partyId>` | Change name of political party |
| **DELETE** | `/api/v1/deleteParty/<partyid>` | Delete political party |
| **POST** | `/api/v1/offices` | Create political office |
| **GET** | `/api/v1/getoffices` | Get political office |
| **GET** | `/api/v1/specificoffice/<int:office_id>` | Get specific political office |

