import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
