from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import config
import pickle
import json

def authenticate():
    token_path = 'token.pickle'           # Path to your pickle token file
    client_secrets_file = 'desk_client.json'  # Your OAuth client secrets file
    scopes = ['https://www.googleapis.com/auth/content']

    creds = None

    # Load credentials from pickle file if exists
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token_file:
            creds = pickle.load(token_file)

    # If there are no valid credentials, or expired token, refresh or run OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
            creds = flow.run_local_server(port=0)

        # Save the credentials to pickle file
        with open(token_path, 'wb') as token_file:
            pickle.dump(creds, token_file)

    return creds
