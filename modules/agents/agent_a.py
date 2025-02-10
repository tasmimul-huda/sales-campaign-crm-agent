from modules.agents.base_agent import BaseAgent
from modules.email.verifier import EmailVerifier
import os
import logging
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()

class AgentA(BaseAgent):
    def __init__(self):
        super().__init__()
        self.verifier = EmailVerifier(os.getenv("HUNTER_API_KEY"))
    
    def execute_task(self):
        sheet = self.sheet_client.get_sheet(
            self.config["SHEET_ID"], 
            self.config["LEADS_SHEET"]
        )
        records = sheet.get_all_records()
        
        updates = []
        for idx, record in enumerate(records, start=2):
            if not record['Email Verified']:
                result = self.verifier.verify(record['Email'])
                status = 'Y' if result['status'] == 'valid' else 'N'
                updates.append({
                    'range': f"F{idx}",
                    'values': [[status]]
                })
        
        if updates:
            self.sheet_client.batch_update(sheet, updates)
            # logger.info(f"Agent A updated {len(updates)} records")