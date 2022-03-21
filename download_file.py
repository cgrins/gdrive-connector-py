import io

import polars as pl

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from get_credentials import get_credentials

SCOPES = ['https://www.googleapis.com/auth/drive']

FILE_ID = '1l2xMTFZNWz6-8DtDlnjEWeWmKuAjJu7N'
SPREADSHEET_MIME_TYPE = 'application/vnd.google-apps.spreadsheet'
CSV_MIME_TYPE = 'text/csv'


def get_spreadsheet(file_id):
    creds = get_credentials(SCOPES)
    fh = io.BytesIO()
    try:
        service = build('drive', 'v3', credentials=creds)

        request = service.files().export_media(fileId=file_id, mimeType=CSV_MIME_TYPE)
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("status=%s", status)
    except HttpError as error:
        print(f'An error occurred: {error}')
    return fh


def get_csv(file_id):
    creds = get_credentials(SCOPES)
    fh = io.BytesIO()
    try:
        service = build('drive', 'v3', credentials=creds)
        request = service.files().get_media(fileId=file_id)
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("status=%s", status)
    except HttpError as error:
        print(f'An error occurred: {error}')
    return fh


def get_file_io(file_id, mime_type):
    print(file_id, mime_type)
    if mime_type == SPREADSHEET_MIME_TYPE:
        return get_spreadsheet(file_id)
    elif mime_type == CSV_MIME_TYPE:
        return get_csv(file_id)
    else:
        print("unknown mimetype")
