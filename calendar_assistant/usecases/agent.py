from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.render import format_tool_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
import os
from .calendar_tools import GetCalendarEventsTool

# Get from environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL")  # "gpt-3.5-turbo-0613"

def run_agent_executor(input='Get me all the calendar events.'):
    # Options
    llm = ChatOpenAI(temperature=0, model=OPENAI_MODEL, api_key=OPENAI_API_KEY)
    tools = [
        GetCalendarEventsTool()
    ]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful and friendly Google Calendar assistant"),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    functions = [format_tool_to_openai_function(t) for t in tools]

    llm_with_tools = llm.bind(functions=functions)

    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    result = agent_executor.invoke({"input": input})

    return result.get("output")