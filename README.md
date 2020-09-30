# Persons API

This API provides functionality of addind, updating and deleting user data.
Following methods are supported:

#### Jwt token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/api-token-auth/` | Request jwt token

#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/v1/persons/` | List existing user ids
POST | `/api/v1/persons/` | Creates a user with provided name and surname
GET | `/api/v1/persons/<person_id>/` | Returns user name, surname and has_vector flag by id
PUT | `/api/v1/persons/` | Adds a serialized image to the user vecrot field
GET | `/api/v1/persons/compare/<person_id1>/<person_id2>/` | Returns euclidian distance between users' vectors
DELETE | `/api/v1/persons/<person_id>/` | Deletes a user
