from dotenv import load_dotenv
from openai import OpenAI
import os


class OpenAIClientSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            load_dotenv()
            api_key = os.environ.get('OPENAI_API_KEY')
            if not api_key:
                raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
            cls._instance = OpenAI(api_key=api_key)
        return cls._instance
