
import os
from dotenv import load_dotenv


from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SERVICE_ACCOUNT_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar",
          "https://www.googleapis.com/auth/calendar.acls"]
CREDS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

CALENDAR_ID = os.getenv("INITIAL_GCAL_ID")
def fetch_email(all_names=list, new_calendar=str):
    CALENDAR_ID = new_calendar
    calendar_service = build("calendar", "v3", credentials=CREDS)
   
    try:
        acl = calendar_service.acl().list(calendarId=CALENDAR_ID).execute()
        user_emails = [item["id"].replace("user:", "") for item in acl["items"]]
        print(user_emails)

        return "Success"
    except HttpError as err:
        print(err)
        return f"Error: {err}", 400