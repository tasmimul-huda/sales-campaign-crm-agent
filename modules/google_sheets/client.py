# --------------------------
# Module 1: Google Sheets Client
# --------------------------
# client.py

import gspread
from dotenv import load_dotenv
import os
import gspread
from typing import List, Dict

from google.oauth2 import service_account

load_dotenv()


class GoogleSheetClient:
    def __init__(self, credentials_file: str, sheet_id: str):
        self.credentials_file = credentials_file
        self.sheet_id = sheet_id
        self.client = self._authenticate()
        
    def _authenticate(self):
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            # "https://www.googleapis.com/auth/drive"
        ]
        creds = service_account.Credentials.from_service_account_file(self.credentials_file, scopes=scope)

        return gspread.authorize(creds)
    
    def get_sheet(self, sheet_name: str):
        return self.client.open_by_key(self.sheet_id).worksheet(sheet_name)
    
    def get_all_records(self, sheet_name: str) -> List[Dict]:
        worksheet = self.get_sheet(sheet_name)
        return worksheet.get_all_records()
    
    def update_cell(self, sheet_name: str, row: int, col: int, value: str):
        worksheet = self.get_sheet(sheet_name)
        worksheet.update_cell(row, col, value)
    
    def append_row(self, sheet_name: str, values: List):
        worksheet = self.get_sheet(sheet_name)
        worksheet.append_row(values)


# if __name__ == "__main__":
#     gs_client = GoogleSheetClient(credentials_file='credentials.json', sheet_id = '1jHJQN7zLz__xPSFofx_3gyICv1jJVDiGpbTBVYYTduk')
#     data = gs_client.get_all_records('Leads')
#     print(data)
#     gs_client.update_cell(sheet_name= 'Leads', row= 2, col=6, value= 'Y')
#     print(data)