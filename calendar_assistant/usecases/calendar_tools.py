from typing import Type, Optional
from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from .calendar_functions import get_calendar_events


class GetCalendarEventsTool(BaseTool):
    name = "get_calendar_events"
    description = """
        Useful when you want to get calendar events.
        """

    def _run(self, query: str):
        events_response = get_calendar_events()
        return events_response

    def _arun(self):
        raise NotImplementedError("get_calendar_events does not support async")