# Unibeez Conversation Tagging

This project tags customer conversations into categories using rules and AI. 

## 📄 rules.json
- Stores all tags (e.g., `hot_buyer`, `just_browsing`, `sign_up!`).  
- Each tag has a list of keywords/phrases.  
- Easy for non-technical staff to edit without touching code.  

## tagger.py
- Reads `rules.json` and applies keyword rules to text.  
- If no match, falls back to a low-cost AI model.  
- Ensures AI only picks from the approved list of tags.  

## monitor.py
- Tests the system with sample text.  
- Reports key metrics: precision, coverage, and AI usage.  
- Helps track accuracy and cost savings.  

## Editing Tags (for staff)
- Open **rules.json** in a text editor (Notepad, VS Code, etc.).  
- Find the `"keywords"` list for the tag you want to update.  
- Add or remove phrases in plain English (inside quotes).  
- Save the file — changes take effect immediately when scripts run.  
