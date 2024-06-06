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
- Other dependencies as listed in `requirements.txt`

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/rit-upy/Accuknox-2.git
   ```
2. Navigate into the project directory:
   ```bash
   cd Accuknox-2
   ```
3. Create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory and add your environment variables:
   ```plaintext
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   ```

## Usage

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Friend Requests

- **Send Friend Request**
  - URL: `/send/`
  - Method: `POST`
  - Body: `{"friend": "<friend_id>"}`
- **Accept Friend Request**
  - URL: `/accept/<int:id>/`
  - Method: `PUT`
- **Reject Friend Request**
  - URL: `/reject/<int:id>/`
  - Method: `DELETE`
- **List Friends**
  - URL: `/list/<str:pending_status>/`
  - Method: `GET`

## Running Tests

1. Run the tests:
   ```bash
   python manage.py test
   ```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
