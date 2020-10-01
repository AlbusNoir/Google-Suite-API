from __future__ import print_function
from pprint import pprint
from googleapiclient import discovery
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = discovery.build('sheets', 'v4', credentials=creds)

# The ID of the spreadsheet containing the sheet to copy.
spreadsheet_id = ''  # this is after d/ in the urlbar

# The ID of the sheet to copy.
sheet_id1 = 0  # this is found following gid= in the url
sheet_id2 = 0  # testing copy multi sheets


copy_sheet_to_another_spreadsheet_request_body = {
    # The ID of the spreadsheet to copy the sheet to.
    'destination_spreadsheet_id': '',  # after /d in urlbar

    # TODO: Add desired entries to the request body.
}

request1 = service.spreadsheets().sheets().copyTo(spreadsheetId=spreadsheet_id, sheetId=sheet_id1, body=copy_sheet_to_another_spreadsheet_request_body)
request2 = service.spreadsheets().sheets().copyTo(spreadsheetId=spreadsheet_id, sheetId=sheet_id2, body=copy_sheet_to_another_spreadsheet_request_body)
response1 = request1.execute()
response2 = request2.execute()


pprint(response1)
pprint(response2)


# TODO: Change spreadsheet_id to input
# TODO: Change destination_spreadsheet_id to input
# TODO: Change sheet_id to input and tell user where to find this info
# TODO: Add a for loop to the sheet_ids?? Pass the user's input into a list and iterate the list
