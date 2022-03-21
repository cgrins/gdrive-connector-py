from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from get_credentials import get_credentials

SCOPES = ['https://www.googleapis.com/auth/drive']


def get_files():
    creds = get_credentials(SCOPES)
    try:
        service = build('drive', 'v3', credentials=creds)
        results = service.files().list(
            fields="nextPageToken, files(id, name, mimeType)",
            q="mimeType = 'application/vnd.google-apps.spreadsheet' or mimeType = 'text/csv'"

        ).execute()
        next_token = results.get('nextPageToken')
        print("next_token='{}'".format(next_token))
        items = results.get('files', [])
        for item in items:
            print(item)

        if not items:
            print('No files found.')
            return
        return items
    except HttpError as error:
        print(f'An error occurred: {error}')
