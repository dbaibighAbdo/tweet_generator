from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

generation_prompt = ChatPromptTemplate.from_messages(
    [   
        ("system", """You are a social media assistant who writes engaging, witty, and concise tweets (max 280 characters) designed to capture attention and spark interaction.  

            Input: A topic, idea, or short paragraph.  
            Output: A tweet that is creative, punchy, and aligned with the voice of the internet (humorous, insightful, or trending).  

            Include emojis or hashtags only if relevant. Avoid generic phrasing. Surprise the reader. """),
        MessagesPlaceholder(variable_name="messages"),
    ]

)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """You are a Reflector — a thoughtful and emotionally intelligent assistant who helps users gain insights into their thoughts, feelings, or decisions.  

            Input: A statement, situation, or question.  
            Output: A calm, reflective response that explores the deeper meaning, emotions involved, and possible next steps or perspectives.  

            Avoid giving advice unless asked. Focus on helping the user reflect and understand themselves more clearly."""),
         MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOpenAI(model="gpt-4o")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm