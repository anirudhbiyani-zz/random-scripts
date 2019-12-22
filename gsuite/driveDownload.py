#!/usr/bin/env python

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import AuthorizedSession
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import errors
import io

__author__ = "Aniruddha Biyani"
__version__ = "1.0.0"
__maintainer__ = "Aniruddha Biyani"
__email__ = "contact@anirudbiyani.com"
__status__ = "Active"

# To download a Google Doc/PPT/Sheet in PDF format via API. 

def main():
   user_id = '' # UserID of the person who own the file or has access to the file.
   SCOPES = ['https://www.googleapis.com/auth/drive']

   credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scopes=SCOPES)
   delegated_credentials = credentials.create_delegated(user_id)
   service = build('drive','v3', credentials=delegated_credentials)

   fileID = "" # The Google File ID

   request = service.files().export_media(fileId=fileID, mimeType='application/pdf')
   fh = io.FileIO('output.pdf', 'wb')
   downloader = MediaIoBaseDownload(fh, request)
   done = False
   while done is False:
       status, done = downloader.next_chunk()
       print "Download %d%%." % int(status.progress() * 100)

if __name__ == '__main__':
    main()
