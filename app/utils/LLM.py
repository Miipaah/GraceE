#Basic Request
#TODO HTTP Request OpenAI GPT 4o Mini with Prompt

from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import asyncio

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

async def send_GPT_chat(command, user_content):
    
    system_prompt = await build_prompt()
     #Send Command to GPT-4o-Mini
    completion = client.chat.completions.create(
    model="gpt-4o-mini",messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content":f"{command}:{user_content}"}
  ]
)
    return completion.choices[0].response

async def build_prompt():
    with open('app\Templates\prompt.json') as raw_prompt_data:
        data = json.load(raw_prompt_data)

        print(data)
    pass

build_prompt()