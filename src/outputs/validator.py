thonpython
def validate_lead(lead: dict):
 email = lead.get("email")
 if not email or "@" not in email:
 return False
 return True