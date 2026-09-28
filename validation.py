def get_amount():
    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return None

        return amount

    except ValueError:
        print("Please enter a valid amount.")
        return None


def get_text(message):
    while True:
        value = input(message)

        if value != "":
            return value

        print("This field cannot be empty.")