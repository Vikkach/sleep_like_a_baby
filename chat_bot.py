import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def collect_messages(context, temperature=0):
    prompt = input()
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = get_completion_from_messages(context, temperature=temperature)
    context.append({'role': 'assistant', 'content': f"{response}"})
    return response
