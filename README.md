
# political_arena

[![Maintainability](https://api.codeclimate.com/v1/badges/930de259caf8289c8cc0/maintainability)](https://codeclimate.com/github/kamaathedj/political_arena/maintainability) [![Build Status](https://travis-ci.org/kamaathedj/political_arena.svg?branch=Development)](https://travis-ci.org/kamaathedj/political_arena) [![Coverage Status](https://coveralls.io/repos/github/kamaathedj/political_arena/badge.svg?branch=Development)](https://coveralls.io/github/kamaathedj/political_arena?branch=Development)

## Description
Politico enables citizens give their mandate to politicians running for different government offices
while building trust in the process through transparency.
## API Endpoints V1

| **METHODS** | **LINKS** | **DESCRIPTION** |
| --- | --- | --- |
| **POST** | `/api/v1/parties` | Create political party |
| **GET** | `/api/v1/parties` | Get political party |
| **GET** | `/api/v1/party/<int:party_id>` | Get specific political party |
| **PATCH** | `/api/v1/parties/<int:partyId>` | Change name of political party |
| **DELETE** | `/api/v1/Parties/<int:partyid>` | Delete political party |
| **POST** | `/api/v1/offices` | Create political office |
| **GET** | `/api/v1/offices` | Get political office |
| **GET** | `/api/v1/offices/<int:office_id>` | Get specific political office |


### Installation, Running and Testing the Api
###### fork the repository and clone it to your computer
```
cd into political_arena
```
###### create virtual enviroment
```
virtualenv venv
```
###### Activate the virtual enviroment
```
For windows
venv/Script/activate

for unix related systems
venv/bin/activate
```

###### Running the Api

```
flask run
```
### Running Api with enviromental variables


| **Enviromental variable** | **Debug** | **DESCRIPTION** |
| --- | --- | --- |
| **production** | `False` | Used when deploying to the internet |
| **development** | `True` | Used during active development of the system |
| **testing** | `True` | Used when testing the system |

###### Create the .env file in the root of the project and pass the enviromental variable you want to run the Api in.
```
export FLASK_ENV=development
```
###### learn more about enviromental variables
[https://github.com/dwyl/learn-environment-variables/blob/master/README.md]

*Note : Things like secret key and database uri can be kept in enviromental variables e.g uri for both database for development and production*
### Testing the Api
```
pytest
```
#### Using postman to consume endpoint and data

###### Getting party endpoints
```{
{
"id":1,
"name":"Odm",
"hqAddress":"Runda",
"logoUrl":"www.odm.com/default/odm.jpg"
}
```
###### Getting office endpoints
```{
{
"id":1,
"name":"president",
"type":"Head of state"
}
```

