import os
import time
import random
import requests
from llm_client import BaseLLMClient


class HuggingFaceLLMClient(BaseLLMClient):
    """Hugging Face Inference API LLM Client Implementation"""

    def __init__(self, api_token: str = None, model_name: str = "microsoft/DialoGPT-medium"):
        self.api_token = api_token or os.getenv("HF_API_TOKEN")
        self.model_name = model_name
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"

    def get_response(self, prompt: str) -> str:
        if not self.api_token:
            return "Error getting response from HuggingFace: Missing HF_API_TOKEN"

        headers = {"Authorization": f"Bearer {self.api_token}"}

        # Prepare the payload for text generation
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 512,
                "temperature": 0.7,
                "do_sample": True,
                "return_full_text": False
            }
        }

        max_retries = 3
        retry_delay = 1

        for attempt in range(max_retries):
            try:
                response = requests.post(self.api_url, headers=headers, json=payload, timeout=30)
                response.raise_for_status()

                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    generated_text = result[0].get("generated_text", "")
                    if generated_text:
                        return generated_text.strip()

                return "Error: Unexpected response format from HuggingFace API"

            except requests.exceptions.HTTPError as e:
                if response.status_code == 503:
                    # Model is loading, wait and retry
                    if attempt < max_retries - 1:
                        wait_time = retry_delay * (2 ** attempt) + random.uniform(0, 1)
                        time.sleep(wait_time)
                        continue
                    else:
                        return f"Error: HuggingFace model {self.model_name} is currently loading. Please try again later."
                elif response.status_code == 429:
                    # Rate limit
                    if attempt < max_retries - 1:
                        wait_time = 60
                        time.sleep(wait_time)
                        continue
                    else:
                        return "Error: HuggingFace API rate limit exceeded."
                else:
                    return f"Error getting response from HuggingFace: HTTP {response.status_code}"

            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    continue
                else:
                    return f"Error getting response from HuggingFace: {str(e)}"

        return f"Error: Failed to get response from HuggingFace after {max_retries} retries"

    def get_model_name(self) -> str:
        return self.model_name
