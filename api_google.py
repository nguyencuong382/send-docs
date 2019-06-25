from __future__ import print_function

from googleapiclient import discovery
from httplib2 import Http


def export_file(fileId, save_file=False):
    SCOPES = 'https://www.googleapis.com/auth/drive'

    from oauth2client import file, client, tools

    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

    content = DRIVE.files().export(fileId=fileId, mimeType='text/html').execute()

    if save_file:
        with open('export.html', 'wb') as file:
            file.write(content)
    return content
