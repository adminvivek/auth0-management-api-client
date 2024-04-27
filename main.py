import requests
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Auth0 credentials
AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
AUDIENCE = f'https://{AUTH0_DOMAIN}/api/v2/'

# Auth0 API endpoints
TOKEN_URL = f'https://{AUTH0_DOMAIN}/oauth/token'
USERS_URL = f'{AUDIENCE}users'

def get_access_token():
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'audience': AUDIENCE,
        'grant_type': 'client_credentials'
    }
    response = requests.post(TOKEN_URL, json=payload)
    token_data = response.json()
    if 'access_token' in token_data:
        return token_data['access_token']
    else:
        print("Error getting access token:", token_data)
        return None


def get_users():
    access_token = get_access_token()
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(USERS_URL, headers=headers)
    return response.json()

def create_user(user_data):
    access_token = get_access_token()
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
    response = requests.post(USERS_URL, headers=headers, data=json.dumps(user_data))
    return response.json()

def delete_user(user_id):
    access_token = get_access_token()
    headers = {'Authorization': f'Bearer {access_token}'}
    delete_url = f'{USERS_URL}/{user_id}'
    response = requests.delete(delete_url, headers=headers)
    return response.status_code

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py [get_users|create_user|delete_user]")
        sys.exit(1)

    action = sys.argv[1]

    if action == 'get_users':
        print("Current users:")
        print(get_users())
    elif action == 'create_user':
        new_user_data = {
            "email": "newuser@example.com",
            "password": "P@ssw0rd",
            "connection": "Username-Password-Authentication"
        }
        print("Creating user:")
        print(create_user(new_user_data))
    elif action == 'delete_user':
        # Replace 'user_id' with actual user ID
        user_id = "user_id"
        print("Deleting user:")
        print(delete_user(user_id))
    else:
        print("Invalid action:", action)
