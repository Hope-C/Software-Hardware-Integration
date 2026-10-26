import os
import sys
from dotenv import load_dotenv
from ollama import Client

# Load local environment variables
load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "tinyllama")

client = Client(host=OLLAMA_HOST)

def generate_ai_response(prompt: str):
    """Sends a prompt to the local Ollama instance and streams the response."""
    print(f"\n[Pi AI - {MODEL_NAME}]: ", end="", flush=True)
    try:
        response_stream = client.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant running locally on a Raspberry Pi."},
                {"role": "user", "content": prompt}
            ],
            stream=True
        )
        for chunk in response_stream:
            print(chunk['message']['content'], end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"\nError communicating with model: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_prompt = " ".join(sys.argv[1:])
        generate_ai_response(user_prompt)
    else:
        print("Usage: python main.py 'Your query here'")

