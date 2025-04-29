from google.oauth2 import service_account
import config

def authenticate():
    credentials = service_account.Credentials.from_service_account_file(
        config.SERVICE_ACCOUNT_FILE, [config.API_SCOPE])
    return credentials