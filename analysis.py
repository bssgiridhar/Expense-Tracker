def show_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print(f"Total expenses: ₹{total:.2f}")


def show_highest(expenses):
    if not expenses:
        print("No expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print(
        f"Highest expense: ₹{highest['amount']:.2f} "
        f"({highest['category']})"
    )


def category_analysis(expenses):
    if not expenses:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category in categories:
            categories[category] = categories[category] + expense["amount"]
        else:
            categories[category] = expense["amount"]

    print("\n----- CATEGORY ANALYSIS -----")

    for category in categories:
        print(f"{category}: ₹{categories[category]:.2f}")