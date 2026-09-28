import json
import os

FILE = "Data/expenses.json"


def load_expenses():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)