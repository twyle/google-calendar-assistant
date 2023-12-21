from ..extensions import google_calendar
from google_calendar.models import Event
from google_calendar.schemas import (
    ListCalendarEvents, ListCalendarEventsResponse
)


def get_calendar_events() -> str:
    req = ListCalendarEvents()
    events_resp: ListCalendarEventsResponse = google_calendar.list_calendar_events(req)
    events: str = "Here are some events from your calendar:\n"
    for event in events_resp.items:
        events += f'{event.summary}\n'
    return events