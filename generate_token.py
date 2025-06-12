from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

SCOPES = ['https://www.googleapis.com/auth/content']

def generate_token():
    flow = InstalledAppFlow.from_client_secrets_file(
        'desk_client.json', SCOPES)
    creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token_file:
        pickle.dump(creds, token_file)
    print("Token generated and saved to token.pickle")

if __name__ == '__main__':
    generate_token()
