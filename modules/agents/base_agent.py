from abc import ABC, abstractmethod
from modules.google_sheets.client import GoogleSheetClient
# from modules.utils.logger import logger
from config.settings import SHEET_CONFIG
import os

class BaseAgent(ABC):
    def __init__(self):
        self.sheet_client = GoogleSheetClient(credentials_file=os.getenv('GOOGLE_CREDENTIALS_PATH'), sheet_id = SHEET_CONFIG.SHEET_ID)
        self.config = SHEET_CONFIG
    
    @abstractmethod
    def execute_task(self):
        pass