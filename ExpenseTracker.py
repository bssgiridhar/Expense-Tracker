from file_handler import load_expenses
from expense_manager import add_expense, view_expenses
from analysis import show_total, show_highest, category_analysis


def print_title():
    print("             EXPENSE TRACKER")
    
# You can select the follwing options which you want to add or modify

def print_menu():
    print()
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Highest Expense")
    print("5. Category Analysis")
    print("6. Exit")
    print()

# Enter your prefered choices

def get_choice():
    choice = input("Enter your choice: ")
    return choice

def show_welcome():
    print()
    print("Welcome to the Expense Tracker")
    print("You can record and analyse your expenses.")
    print()

# Below specify preferred choice

def show_add_message():
    print()
    print("You selected Add Expense.")
    print()


def show_view_message():
    print()
    print("You selected View Expenses.")
    print()


def show_total_message():
    print()
    print("You selected Total Expenses.")
    print()

def show_highest_message():
    print()
    print("You selected Highest Expense.")
    print()


def show_category_message():
    print()
    print("You selected Category Analysis.")
    print()


def show_exit_message():
    print()
    print("Thank you for using Expense Tracker!")
    print("Your expense data has been saved.")
    print()


def invalid_choice():
    print()
    print("Invalid choice.")
    print("Please select a number from 1 to 6.")
    print()

# Below handles the add  expense choice if preferred by you 

def run_add_expense(expenses):
    show_add_message()
    add_expense(expenses)

# Below handles the view expenses choice if preferred by you 

def run_view_expenses(expenses):
    show_view_message()
    view_expenses(expenses)


def run_show_total(expenses):
    show_total_message()
    show_total(expenses)


def run_show_highest(expenses):
    show_highest_message()
    show_highest(expenses)


def run_category_analysis(expenses):
    show_category_message()
    category_analysis(expenses)

# Below decides what action should be performed based on your choice 

def handle_choice(choice, expenses):
    if choice == "1":
        run_add_expense(expenses)

    elif choice == "2":
        run_view_expenses(expenses)

    elif choice == "3":
        run_show_total(expenses)

    elif choice == "4":
        run_show_highest(expenses)

    elif choice == "5":
        run_category_analysis(expenses)

    elif choice == "6":
        return False

    else:
        invalid_choice()

    return True

# Below main function controls the entire expense tracker 

def main():
    expenses = load_expenses()

    show_welcome()

    running = True

    while running:
        print_title()
        print_menu()

        choice = get_choice()

        running = handle_choice(choice, expenses)

# Displays the final message after we choose the exit 

    show_exit_message()



if __name__ == "__main__":
    main()
