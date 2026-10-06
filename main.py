"""Expense Tracker - a simple Python CLI application."""
from storage import load_expenses, save_expenses
from validators import validate_amount, validate_category, validate_date, CATEGORIES


def add_expense(expenses):
    try:
        title = input("Title: ").strip()
        if not title:
            raise ValueError("Title cannot be empty.")
        amount = validate_amount(input("Amount: "))
        category = validate_category(input(f"Category ({'/'.join(CATEGORIES)}): "))
        date = validate_date(input("Date YYYY-MM-DD (Enter for today): "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    next_id = max((e["id"] for e in expenses), default=0) + 1
    expenses.append({"id": next_id, "title": title, "amount": amount,
                     "category": category, "date": date})
    save_expenses(expenses)
    print("Expense added.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    print(f"\n{'ID':<4}{'Date':<12}{'Category':<10}{'Amount':>9}  Title")
    for e in expenses:
        print(f"{e['id']:<4}{e['date']:<12}{e['category']:<10}{e['amount']:>9.2f}  {e['title']}")


def delete_expense(expenses):
    try:
        expense_id = int(input("ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    for e in expenses:
        if e["id"] == expense_id:
            expenses.remove(e)
            save_expenses(expenses)
            print("Deleted.")
            return
    print("No expense with that ID.")