# AI-Driven Lead Management & Outreach Automation

## Overview
This project automates the lead processing workflow using AI agents to streamline email validation, sales outreach, and campaign tracking. The system monitors an online Excel file for new leads, assigns verification and outreach tasks to agents, and consolidates results into the Excel file or via email.

## Workflow

1. **Supervisor Agent**  
   - Monitors an online Excel file (Google Sheets).  
   - Assigns leads to **Agent A** for verification.  
   - Passes verified leads to **Agent B** for outreach.  
   - Consolidates updates from agents and generates reports.  

2. **Agent A (Lead Verifier)**  
   - Verifies email addresses and contact details using external validation tools(Hunter API).  
   - Updates the lead status in the Excel file.  

3. **Agent B (Outreach Specialist)**  
   - Sends personalized sales emails to verified leads.  
   - Captures lead responses (Interested, Not Interested, No Response). (not implemented yet)  
   - Updates the response status in the Excel file. (not implemented yet)  

4. **Supervisor Agent (Report Generation)**  
   - Monitors updates from agents and summarizes campaign progress.  
   - Writes consolidated results into the online Excel file or emails a report to stakeholders.  

## Technologies Used

- **Automation & Integration:** Python (schedule, apscheduler), Zapier, Integromat  
- **Online Excel Handling:** Google Sheets API, Microsoft Graph API  
- **Email Verification:** Hunter.io API, NeverBounce API  
- **Email Automation:** SendGrid, AWS SES, Custom SMTP scripts

## Setup Instructions
Comming...
