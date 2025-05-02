from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import config
import token
import json

def authenticate():
    creds = None
    token_file = 'token.json'
    client_file = 'client.json'
    
    if os.path.exists(client_file):
        with open(client_file, 'r') as f:
            client_data = json.load(f)["web"]

    if os.path.exists(token_file):
        with open(token_file, 'r') as f:
            token_data = json.load(f)
        creds = Credentials(
            token=token_data.get("access_token"),
            refresh_token=token_data.get("refresh_token"),
            token_uri='https://oauth2.googleapis.com/token',
            client_id=client_data["client_id"],
            client_secret=client_data["client_secret"],
            scopes=['https://www.googleapis.com/auth/content']
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                config.CLIENT_SECRETS_FILE, 
                [config.API_SCOPE],
                redirect_uri="https://localhost:8080"
            )
            creds = flow.run_local_server(port=0)
        
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    return creds
