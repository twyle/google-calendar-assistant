from google_calendar import GoogleCalendar
import os

client_secret: str = os.environ['CLIENT_SECRET_FILE']
google_calendar: GoogleCalendar = GoogleCalendar(secret_file=client_secret)
google_calendar.authenticate()