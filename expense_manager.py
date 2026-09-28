from datetime import datetime
from file_handler import save_expenses
from validation import get_amount, get_text


def add_expense(expenses):
    amount = get_amount()

    if amount is None:
        return

    category = get_text("Enter category: ")
    note = get_text("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n----- ALL EXPENSES -----")

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. ₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['note']} | "
            f"{expense['date']}"
        )