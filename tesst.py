from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive.file']

def authenticate_google_api():
    """Shows basic usage of the Google Docs API.
    Returns an authenticated service.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def create_google_doc(service):
    # Create a new Google Doc
    document = service.documents().create(body={'title': 'My New Doc'}).execute()
    document_id = document.get('documentId')

    # Insert the text 'Dogs and cats' into the document
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': 'Dogs and cats'
            }
        }
    ]

    result = service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()

    print(f'Document created and updated with ID: {document_id}')
    return document_id

def main():
    # Authenticate and create the Google Docs API service
    creds = authenticate_google_api()
    service = build('docs', 'v1', credentials=creds)

    # Create a new Google Doc with 'Dogs and cats' written in it
    create_google_doc(service)

if __name__ == '__main__':
    main()
