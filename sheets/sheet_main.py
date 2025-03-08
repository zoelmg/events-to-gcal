from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re
from database.models import Users
from gcal import gcal_main
from dotenv import load_dotenv
import os


# Path to your service account JSON key
SERVICE_ACCOUNT_FILE = "credentials.json"

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = os.getenv("INITIAL_SHEET_ID")
CREDS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def instantiate_service():
    
    # Create Google Sheets API service
    try: 
        sheets_service = build("sheets", "v4", credentials=CREDS)

        result = sheets_service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get("values", [])

        print("Google Sheets Data:", values)
    except HttpError as err:
        print(err)

def populate_user_table(new_sheet:str, new_calendar:str):
    SPREADSHEET_ID = new_sheet
    sheets_service = None
    range_name = "Burn Out Sheet!2:2"
    try:
        sheets_service = build("sheets", "v4", credentials=CREDS)
    except HttpError as err:
        return f"Error: Tried to instantiate sheet service, failed to do so\n{err}", 400
    

    try:
        result = sheets_service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
    except HttpError as err:
        print(err)
        return f"Error: Tried to fetch everyone's names from the google sheet, failed to do so\n{err}", 400
    
    values = result.get('values', [])
    flat_values = values[0]
    print(flat_values)
    all_names = []

    for person in flat_values:
        person = person.lower()
        person = person.replace(" ", "").replace("\n", "")
        names = re.split(r'[**]', person)
        names = [name for name in names if name]
        all_names.append(names)

    
    print(all_names)
    try: 
        email=gcal_main.fetch_email(all_names, new_calendar)
        print(email)
        #user = Users(nickname=names[0], name=names[1], email=gcal_main.fetch_email(names[0], new_calendar))
    except:
        return "Error: Tried to create a person but failed to do so", 400

        
            
        #print(names)

    return "Success"

    

 
    

    



    
    
