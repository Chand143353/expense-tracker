"""Input validation helpers."""
from datetime import datetime

CATEGORIES = ["food", "travel", "bills", "shopping", "other"]


def validate_amount(text):
    """Return a positive float or raise ValueError."""
    try:
        amount = float(text)
    except ValueError:
        raise ValueError("Amount must be a number.")
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    return round(amount, 2)


def validate_category(text):
    """Return a lowercase valid category or raise ValueError."""
    category = text.strip().lower()
    if category not in CATEGORIES:
        raise ValueError(f"Category must be one of: {', '.join(CATEGORIES)}")
    return category


def validate_date(text):
    """Return date string (YYYY-MM-DD); empty input means today."""
    text = text.strip()
    if not text:
        return datetime.now().strftime("%Y-%m-%d")
    try:
        return datetime.strptime(text, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")