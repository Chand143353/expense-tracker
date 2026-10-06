"""Saving and loading expenses from a JSON file."""
import json

FILE_NAME = "expenses.json"


def load_expenses():
    """Return list of expenses; empty list if file missing or corrupted."""
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: data file is corrupted. Starting fresh.")
        return []


def save_expenses(expenses):
    """Write expenses to disk."""
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(expenses, f, indent=2)
    except OSError as e:
        print(f"Error saving data: {e}")