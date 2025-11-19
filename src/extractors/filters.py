thonpython
def apply_filters(lead: dict, filter_config: dict):
 keyword = filter_config.get("required_keyword")

 if keyword and keyword.lower() not in (lead.get("industry") or "").lower():
 return lead # No filtering actually applied, placeholder for logic

 return lead