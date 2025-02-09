import requests
from dotenv import load_dotenv
# from modules.utils.logger import logger
import os
load_dotenv()

class EmailVerifier:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.hunter.io/v2/email-verifier"
    
    def verify(self, email: str) -> dict:
        try:
            response = requests.get(
                f"{self.base_url}?email={email}&api_key={self.api_key}",
                timeout=10
            )
            response.raise_for_status()
            return response.json()['data']
        except Exception as e:
            # logger.error(f"Verification failed for {email}: {str(e)}")
            return {"status": "unknown"}
        
