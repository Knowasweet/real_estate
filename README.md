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
- Docker, docker-compose, Makefile
- NGINX
- Celery, Flower
- Redis
- Pytest with factories and fixtures

## Docker Build Setup

```
docker compose up --build -d --remove-orphans
```
Makefile:
```
make build
```

## Application API

### 1. Users
1.1 User registration.
Creates a new user with sending an email to the Mailtrap service for subsequent activation.

```
POST api/v1/auth/users/
```

**Body**

| Name        | Type  | Description     | Required field |
|-------------|-------|-----------------|----------------|
| email       | Email | email           | +              |
| username    | Char  | username        | +              |
| first_name  | Char  | first_name      | +              |
| second_name | Char  | second_name     | +              |
| password    | Char  | password        | +              |
| re_password | Char  | repeat password | +              |

**Response**

| Name        | Description |
|-------------|-------------|
| username    | username    |
| first_name  | name        |
| second_name | surname     |
| email       | email       |
| pkid        | primary key |

1.2 User activation.
Activation takes data from the link that went to Mailtrap.

```
POST api/v1/auth/users/activation/
```
**Body**

| Name  | Type | Description | Required field |
|-------|------|-------------|----------------|
| uid   | Char | uid         | +              |
| token | UUID | token       | +              |

1.3 Creating a token.

```
POST api/v1/auth/jwt/create/
```
**Body**

| Name     | Type  | Description | Required field |
|----------|-------|-------------|----------------|
| email    | Email | email       | +              |
| password | Char  | password    | +              |

**Response**

| Name    | Description |
|---------|-------------|
| refresh | username    |
| access  | name        |

The access field uses JSON Web Token authentication from Djoser.

### 2. Profiles

2.1 Self profile.
```
GET api/v1/profile/me/
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

2.2 Updating your profile.

```
PATCH api/v1/profile/update/<str:username>/
```
**Body**

| Name          | Type        | Description   | 
|---------------|-------------|---------------|
| phone_number  | PhoneNumber | phone number  |
| profile_image | Image       | profile photo |
| about_me      | Char        | description   |
| gender        | Char        | gender        | 
| country       | Country     | country       |
| city          | Char        | city          |
| buyer         | Boolean     | buyer         |
| agent         | Boolean     | agent         |
| buyer         | Boolean     | buyer         |
| license       | Char        | license       | 

**Response**

| Name          | Description   |
|---------------|---------------|
| phone_number  | phone number  |
| profile_image | profile photo |
| about_me      | description   |
| gender        | gender        |
| country       | country       |
| city          | city          |
| buyer         | buyer         |
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


2.4 List of top agents

```
GET api/v1/profile/agents/top
```

The same Response as in paragraph 2.3

### 3. Properties
3.1 Create the property
```
POST api/v1/properties/create/
```
**Body**

| Name             | Type     | Description        | Required field |
|------------------|----------|--------------------|----------------|
| title            | Char     | name property      | +              |
| country          | Country  | country            | -              |
| city             | Char     | city               | -              |
| property_street  | Char     | property street    | -              |
| property_number  | Integer  | property number    | -              |
| price            | Decimal  | price              | -              |
| property_tax     | Decimal  | property tax       | -              |
| advert_type      | Char     | advert type        | -              |
| property_type    | Char     | property tax       | -              |
| main_photo       | Image    | main photo         | -              |
| photo1           | Image    | additional photo   | -              |
| photo2           | Image    | additional photo   | -              |
| photo3           | Image    | additional photo   | -              |
| photo4           | Image    | additional photo   | -              |
| published_status | Boolean  | published property | -              |
| bathrooms        | Decimal  | bathrooms          | -              |
| bedrooms         | Integer  | bedrooms           | -              |
| number_of_floors | Integer  | number of floors   | -              |
| plot_area        | Decimal  | plot area          | -              |
| price            | Decimal  | price              | -              |
| description      | Text     | description        | -              |
| postal_code      | Char     | postal code        | -              |

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


3.2 Update the property
```
PUT api/v1/properties/update/<slug:slug>
```
**Body**

| Name             | Type     | Description        | 
|------------------|----------|--------------------|
| title            | Char     | name property      | 
| country          | Country  | country            |
| city             | Char     | city               |
| property_street  | Char     | property street    |
| property_number  | Integer  | property number    |
| price            | Decimal  | price              |
| property_tax     | Decimal  | property tax       |
| advert_type      | Char     | advert type        |
| property_type    | Char     | property tax       |
| main_photo       | Image    | main photo         |
| photo1           | Image    | additional photo   |
| photo2           | Image    | additional photo   |
| photo3           | Image    | additional photo   |
| photo4           | Image    | additional photo   |
| published_status | Boolean  | published property |
| bathrooms        | Decimal  | bathrooms          |
| bedrooms         | Integer  | bedrooms           |
| number_of_floors | Integer  | number of floors   |
| plot_area        | Decimal  | plot area          |
| price            | Decimal  | price              |
| description      | Text     | description        |
| postal_code      | Char     | postal code        |

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
GET api/v1/properties/all/
```

**Response**

The same as in paragraph 3.1


3.5 List of all real estate owned by agents

```
GET api/v1/properties/all/
```

**Response**

The same as in paragraph 3.1

3.6 Real estate search
```
GET api/v1/properties/search/
```

**Response**

The same as in paragraph 3.1

3.7 Viewing real estate details

```
GET api/v1/properties/detail/<slug:slug>
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
| rating  | Integer | rating      | +              |
| comment | Text    | comment     | +              |

**Response**

| Name    | Description |
|---------|-------------|
| message | success     |

### 5. Offers

Send a request for an offer.

```
POST api/v1/offers/
```

**Body**

| Name         | Type        | Description  | Required field |
|--------------|-------------|--------------|----------------|
| name         | Char        | name         | +              |
| email        | Email       | email        | +              |
| subject      | Char        | subject      | +              |
| message      | Text        | message      | +              |
| phone_number | PhoneNumber | phone number | -              |

**Response**

| Name    | Description |
|---------|-------------|
| success | description |