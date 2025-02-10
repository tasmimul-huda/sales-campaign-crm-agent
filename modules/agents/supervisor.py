from modules.agents.base_agent import BaseAgent
import logging
logger = logging.getLogger(__name__)
class Supervisor(BaseAgent):
    def generate_report(self):
        sheet = self.sheet_client.get_sheet(
            self.config["SHEET_ID"], 
            self.config["SUMMARY_SHEET"]
        )
        
        leads_sheet = self.sheet_client.get_sheet(
            self.config["SHEET_ID"], 
            self.config["LEADS_SHEET"]
        )
        
        records = leads_sheet.get_all_records()
        summary = {
            'total': len(records),
            'verified': sum(1 for r in records if r['Email Verified'] == 'Y'),
            'responded': sum(1 for r in records if r['Response Status'])
        }
        
        sheet.clear()
        sheet.append_row(["Metric", "Value"])
        sheet.append_rows([
            ["Total Leads", summary['total']],
            ["Verified Leads", summary['verified']],
            ["Responded Leads", summary['responded']]
        ])
        
        # logger.info("Supervisor generated summary report")