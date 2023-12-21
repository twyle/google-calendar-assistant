from dotenv import load_dotenv
load_dotenv()

from calendar_assistant.usecases.calendar_functions import get_calendar_events
from calendar_assistant.usecases.agent import run_agent_executor

print(run_agent_executor())