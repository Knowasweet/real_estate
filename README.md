#Real estate app

The real estate service provides a RESTful API that allows:

1) Buyers view real estate.

2) Agents promote themselves as a qualified specialist and provide their services.

3) Sellers to sell property.

4) Give absolutely everyone a rating to agents, as well as request preferences for improving the service.

## Technical stack, technologies

<img src="img.png" width='400' />

- Python 3.10
- Django
- Django Rest Framework
- PostgreSQL
- Docker, Makefile, docker-compose
- NGINX
- Celery, Flower
- Redis
- Pytest with factories and fixtures

## Docker Build Setup

```
docker compose up -d --remove-orphans
```
Makefile:
```
make build
```

## Application API

### 1. Users
1.1 User registration.
Creates a new user with sending an email.

```
POST api/v1/auth/users/
```

**Body**

| Name        | Type     | Description     | Required field |
|-------------|----------|-----------------|----------------|
| email       | string   | email           | +              |
| username    | string   | username        | +              |
| first_name  | string   | name            | +              |
| second_name | string   | surname         | +              |
| password    | string   | password        | +              |
| re_password | string   | repeat password | +              |

**Response**

| Name        | Description |
|-------------|-------------|
| pkid        | primary key |
| username    | username    |
| first_name  | name        |
| second_name | surname     |
| email       | email       |


1.2 Login. Creating a token.

```
POST api/v1/auth/jwt/create/
```
**Body**

| Name     | Type     | Description | Required field |
|----------|----------|-------------|----------------|
| email    | string   | email       | +              |
| password | string   | password    | +              |

**Response**

| Name     | Description   |
|----------|---------------|
| refresh  | refresh token |
| access   | access token  |

The access field uses JSON Web Token authentication from Djoser.

### 2. Profiles

2.1 Self profile.
```
GET api/v1/profile/
```

**Response**

| Name          | Description       |
|---------------|-------------------|
| id            | id                |
| username      | username          |
| first_name    | name              |
| second_name   | surname           |
| full_name     | name + surname    |
| email         | email             |
| phone_number  | phone number      |
| profile_image | profile photo     |
| about_me      | description       |
| license       | license           |
| gender        | gender            |
| country       | country           |
| city          | city              |
| buyer         | are you a buyer?  |
| seller        | are you a seller? |
| agent         | are you a agent?  |
| rating        | your rating       |
| count_reviews | count reviews     |
| reviews       | reviews           |

2.2 Updating your profile.

```
PATCH api/v1/profile/update/<str:username>/
```
**Body**

| Name          | Type       | Description   | 
|---------------|------------|---------------|
| phone_number  | string     | phone number  |
| profile_image | object     | profile photo |
| about_me      | string     | description   |
| gender        | string     | gender        | 
| country       | string     | country       |
| city          | string     | city          |
| seller        | boolean    | seller        |
| agent         | boolean    | agent         |
| buyer         | boolean    | buyer         |
| license       | string     | license       | 

**Response**

| Name          | Description   |
|---------------|---------------|
| phone_number  | phone number  |
| profile_image | profile photo |
| about_me      | description   |
| gender        | gender        |
| country       | country       |
| city          | city          |
| seller        | seller        |
| agent         | agent         |
| buyer         | buyer         |
| license       | license       |

2.3 List of agents.

```
GET api/v1/profile/agents/
```

**Response**

| Name          | Description       |
|---------------|-------------------|
| username      | username          |
| first_name    | name              |
| second_name   | surname           |
| full_name     | name + surname    |
| email         | email             |
| id            | id                |
| phone_number  | phone number      |
| profile_image | profile photo     |
| about_me      | description       |
| license       | license           |
| gender        | gender            |
| country       | country           |
| city          | city              |
| buyer         | are you a buyer?  |
| seller        | are you a seller? |
| agent         | are you a agent?  |
| rating        | your rating       |
| count_reviews | count reviews     |
| reviews       | reviews           |


2.4 List of top agents.

```
GET api/v1/profile/agents/top
```

The same Response as in paragraph 2.3

### 3. Properties
3.1 Create the property.
```
POST api/v1/properties/create/
```
**Body**

| Name             | Type    | Description                          | Required field |
|------------------|---------|--------------------------------------|----------------|
| title            | string  | name property                        | +              |
| country          | string  | country                              | -              |
| city             | string  | city                                 | -              |
| property_street  | string  | property street                      | -              |
| property_number  | number  | property number                      | -              |
| price            | number  | price                                | -              |
| property_tax     | number  | property tax                         | -              |
| advert_type      | string  | sale/rent/auction                    | -              |
| property_type    | string  | house/apartment/commercial premises/ | -              |
|                  |         | office/warehouse/other               |                |
| main_photo       | object  | main photo                           | -              |
| photo1           | object  | additional photo                     | -              |
| photo2           | object  | additional photo                     | -              |
| photo3           | object  | additional photo                     | -              |
| photo4           | object  | additional photo                     | -              |
| published_status | boolean | published property                   | -              |
| bathrooms        | number  | bathrooms                            | -              |
| bedrooms         | number  | bedrooms                             | -              |
| number_of_floors | number  | number of floors                     | -              |
| plot_area        | number  | plot area                            | -              |
| price            | number  | price                                | -              |
| description      | string  | description                          | -              |
| postal_code      | string  | postal code                          | -              |

**Response**

| Name             | Description        |
|------------------|--------------------|
| id               | id                 |
| user             | user               |
| created_at       | date of creation   |
| title            | name property      |
| slug             | slug               |
| ref_code         | link to properties |
| description      | description        |
| country          | country            |
| city             | city               |
| postal_code      | postal code        |
| property_street  | property street    |
| property_number  | property number    |
| price            | price              |
| property_tax     | property tax       |
| plot_area        | plot area          |
| number_of_floors | number of floors   |
| bedrooms         | bedrooms           |
| bathrooms        | bathrooms          |
| advert_type      | advert type        |
| property_type    | property type      |
| main_photo       | main photo         |
| photo1           | additional photo   |
| photo2           | additional photo   |
| photo3           | additional photo   |
| photo4           | additional photo   |
| published_status | published property |
| views            | number of views    |


3.2 Update a property
```
PUT api/v1/properties/update/<slug:slug>
```
**Body**

| Name             | Type    | Description        | 
|------------------|---------|--------------------|
| title            | string  | property name      | 
| country          | string  | country            |
| city             | string  | city               |
| property_street  | string  | property street    |
| property_number  | number  | property number    |
| price            | number  | price              |
| property_tax     | number  | property tax       |
| advert_type      | string  | advert type        |
| property_type    | string  | property type      |
| main_photo       | object  | main photo         |
| photo1           | object  | additional photo   |
| photo2           | object  | additional photo   |
| photo3           | object  | additional photo   |
| photo4           | object  | additional photo   |
| published_status | boolean | published property |
| bathrooms        | number  | bathrooms          |
| bedrooms         | number  | bedrooms           |
| number_of_floors | number  | number of floors   |
| plot_area        | number  | plot area          |
| description      | string  | description        |
| postal_code      | string  | postal code        |

**Response**

The same as in paragraph 3.1

3.3 Delete property

```
DELETE api/v1/properties/delete/<slug:slug>
```

**Response**

| Name    | Description |
|---------|-------------|
| message | success     |


3.4 List of all properties

```
GET api/v1/properties/
```

**Response**

The same as in paragraph 3.1


3.5 List of all real estate owned by agents

```
GET api/v1/properties/agents/
```

**Response**

The same as in paragraph 3.1

3.6 Viewing real estate details

```
GET api/v1/properties/<slug:slug>
``` 

**Response**

The same as in paragraph 3.1

### 4. Ratings
Set a rating

```
POST api/v1/ratings/<str:profile_id>/
```

**Body**

| Name    | Type    | Description | Required field |
|---------|---------|-------------|----------------|
| rating  | number  | rating      | +              |
| comment | string  | comment     | +              |

**Response**

| Name    | Description |
|---------|-------------|
| message | success     |
