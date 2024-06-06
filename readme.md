# Accuknox Technical Interview

## Description

A Django-based REST API for managing friend requests and friendships. Users can send, accept, and reject friend requests and list their friends.

## Features

- Signup
- Login
- Send friend requests
- Accept friend requests
- Reject friend requests
- List friends based on request status

## Installation

### Prerequisites

- Python 3.x
- Django 3.x
- Docker
- Other dependencies as listed in `requirements.txt`

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/rit-upy/Accuknox-2.git
   ```
2. Navigate into the project directory:
   ```bash
   cd Accuknox-2/api
   ```
3. Build the docker image:
   ```bash
   docker build -t <tagname> .
   ```
4. Run the docker container:
   ```bash
   docker run <tagname>
   ```

## API Endpoints

#Authentication

- **Login**

  - URL: `/api/auth/login/`
  - Method: `POST`
  - Body: `{"email" : "email id"}`

- **Signup**
  - URL: `/api/auth/signup`
  - Method: `POST`
  - Body: `{
"email": "email id",
"password": "password",
"first_name": "First name",
"last_name": "Last Name"
}`

### Friend Requests

- **Send Friend Request**
  - URL: `/send/`
  - Method: `POST`
  - Body: `{"friend": "<friend_id>"}`
- **Accept Friend Request**
  - URL: `/accept/`
  - Method: `PUT`
    -Body: `{"friend": "<friend_id>"}`
- **Reject Friend Request**
  - URL: `/reject/`
  - Method: `DELETE`
  - Body: `{"friend": "<friend_id>"}`
- **List Friends**
  - URL: `/list/<str:pending_status>/`
  - Method: `GET`
  - Body: `{"friend": "<friend_id>"}`

## Notes

- You must login after signing up
- Use the token returned after login to authenticate yourself in Postman
