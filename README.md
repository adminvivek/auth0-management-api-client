# auth0-management-api-client

This Python script provides a client for interacting with the Auth0 Management API. It allows you to perform CRUD (Create, Read, Delete) operations on users in your Auth0 account.

## Prerequisites

Before running the script, ensure you have the following prerequisites:

- Python 3.x installed
- Auth0 account with appropriate permissions
- `.env` file containing Auth0 credentials (`AUTH0_DOMAIN`, `CLIENT_ID`, `CLIENT_SECRET`)

## Installation

1. Clone the repository:

   git clone https://github.com/adminvivek/auth0-management-api-client.git

2. Navigate to the project directory:

   cd auth0-management-api-client

3. Install dependencies:

   pip install -r requirements.txt

## Usage

ou can use the script in three different ways:

1. Running directly from the console with function calls:

   python auth0_script.py get_users
   python auth0_script.py create_user
   python auth0_script.py delete_user

2. Making API calls:
   Use curl commands to interact with the Auth0 Management API. Here are some example commands:

   . Get Users:
   curl -X GET https://YOUR_AUTH0_DOMAIN/api/v2/users -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

   . Create User:
   curl -X POST https://YOUR_AUTH0_DOMAIN/api/v2/users \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
   "email": "newuser@example.com",
   "password": "P@ssw0rd",
   "connection": "Username-Password-Authentication"
   }'

   . Delete User:
   curl -X DELETE https://YOUR_AUTH0_DOMAIN/api/v2/users/YOUR_USER_ID -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

3. Deploying with Docker:

   . Build Docker image:
   docker build -t auth0-management-api-client .

   . Run Docker container:
   docker run auth0-management-api-client get_users
