import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Google Sheets Configuration
SHEET_CONFIG = {
    "SHEET_ID": os.getenv("GOOGLE_SHEET_ID"),
    "LEADS_SHEET": "Leads",
    "SUMMARY_SHEET": "Summary",
   
}

# Email Configuration
EMAIL_CONFIG = {
    "VERIFICATION_API": "hunter",
    "SENDING_SERVICE": "sendgrid",
    "FROM_EMAIL": "campaign@yourcompany.com"
}


#  "COLUMN_MAPPING": {
#         "lead_name": 1,
#         "email": 2,
#         "contact_number": 3,
#         "company": 4,
#         "industry": 5,
#         "email_verified": 6,
#         "response_status": 7,
#         "notes": 8,
#         "assigned_to": 9
#     }