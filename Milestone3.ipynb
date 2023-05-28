import os
import time


api_key = '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'
import openai
import langchain
import os
os.environ["OPENAI_API_KEY"] = api_key

from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=0.5)

template="Let's engage in a debate on whether technology is making us more connected or disconnected. I will take the stance that technology is promoting connectivity initially, and you will argue that it is causing disconnection. We will present our points and counter each other's arguments. The goal is to reach a consensus. Feel free to change your opinion if you find my counters valid."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chain = LLMChain(llm=chat, prompt=chat_prompt)

pro_connected = "I believe that technology is making us more connected because..."
pro_disconnected = "I disagree and argue that technology is making us more disconnected due to..."

for x in range(3):
    print(pro_connected)
    print()
    counter_response = chain.run(input1="connected", input2="disconnected", text=pro_connected)
    print(counter_response)
    print()
    pro_connected = chain.run(input1="disconnected", input2="connected", text=counter_response)
