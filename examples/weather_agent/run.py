import sys
import os
from dotenv import load_dotenv

# setting path
sys.path.append('..\swarm')

from swarm.repl import run_demo_loop
from agents import weather_agent

## Setup the API keys
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    run_demo_loop(weather_agent, stream=True)
