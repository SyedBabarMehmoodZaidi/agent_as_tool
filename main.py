from agents import Agent, Runner
from connection import config

#Define individual translator agents

italian_agent = Agent(
    name="Italian Translator",
    instructions="Translate the following text into Italian.",
)

spainish_agent = Agent(
    name="Spainish Translator",
    instructions="Translate the following text into Spainsh.",
)


arabic_agent = Agent(
    name="Arabic Translator",
    instructions="Translate the following text into Arabic.",
)


urdu_agent = Agent(
    name="Urdu Translator",
    instructions="Translate the following text into Urdu.",
)


french_agent = Agent(
    name="French Translator",
    instructions="Translate the following text into French.",
)

#Main agent that routes to the right translator agent

translation_router = Agent(
    name= "Translation Router",
    instructions="""
You are a translation router.
You will receive a text and the language to translate it into.
You will route the text to the right translator agent based on the language.
If the language is not supported, you will return an error message.
Supported languages: Italian, Spanish, Arabic, Urdu, French.
""",
    tools=[
        #converts these agens into tools
        italian_agent.as_tool(
            tool_name="translate_to_italian",
            tool_description="Translate text to Italian.",

        ),
        spainish_agent.as_tool(
            tool_name="translate_to_spainish",
            tool_description="Translate text to Spainish.",

        ),
        arabic_agent.as_tool(
            tool_name="translate_to_Arabic",
            tool_description="Translate text to Arabic.",

        ),
        urdu_agent.as_tool(
            tool_name="translate_to_Urdu",
            tool_description="Translate text to Urdu.",

        ),
        french_agent.as_tool(
            tool_name="translate_to_French",
            tool_description="Translate text to French.",

        ),

    ]
)

#Example input

result = Runner.run_sync(translation_router,"Translate 'how are you' into Urud.",run_config=config)
print(result.final_output)