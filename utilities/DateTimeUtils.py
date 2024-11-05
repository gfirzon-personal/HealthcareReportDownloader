from datetime import datetime

def get_formatted_dt() -> str:
    """
    Convert a date/time to formatted string.
    """
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    return formatted_datetime

def get_datetime_iso():
    return datetime.now().isoformat()
    