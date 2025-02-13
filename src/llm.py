## OpenAI compatible streaming example
import os
import requests
import json

BASE_URL = "https://nano-gpt.com/api/v1"

def stream_chat_completion(messages, model="chatgpt-4o-latest"):
    API_KEY = os.environ.get("NANOGPT_API_KEY")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream"  # Required for SSE streaming
    }

    """
    Send a streaming chat completion request using the OpenAI-compatible endpoint.

    Args:
        messages (list): List of message dictionaries with 'role' and 'content'
        model (str): Model to use for completion
    """
    data = {
        "model": model,
        "messages": messages,
        "stream": True  # Enable streaming
    }

    # Make streaming request
    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=headers,
        json=data,
        stream=True  # Enable streaming in requests
    )

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")

    # Process the streaming response
    for line in response.iter_lines():
        if line:
            # Remove "data: " prefix
            line = line.decode('utf-8')
            if line.startswith('data: '):
                line = line[6:]

            # Skip "[DONE]" message
            if line == '[DONE]':
                break

            try:
                # Parse the JSON data
                chunk = json.loads(line)
                # Extract the content delta if it exists
                if chunk['choices'][0]['delta'].get('content'):
                    yield chunk['choices'][0]['delta']['content']
            except json.JSONDecodeError:
                continue
