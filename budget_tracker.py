def show_menu():
    print("\n=== Budget Tracker Menu ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")

def get_choice():
    choice = input("Enter your choice (1-5): ")
    return choice

def add_transaction(transactions, t_type, categories):
    while True:
        try:
            amount = float(input(f"Enter {t_type} amount: "))
            if amount <= 0:
                print("Amount must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    print("Select category:")
    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")
    while True:
        cat_choice = input(f"Enter category number (1-{len(categories)}): ")
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            category = categories[int(cat_choice) - 1]
            break
        else:
            print("Invalid category choice. Try again.")

    transaction = {
        "type": t_type,
        "amount": amount,
        "category": category
    }
    transactions.append(transaction)
    print(f"{t_type.capitalize()} added!")

def view_transactions(transactions):
    if not transactions:
        print("No transactions recorded yet.")
        return
    print("\n--- Transactions ---")
    for i, t in enumerate(transactions, start=1):
        print(f"{i}. {t['type'].capitalize()} - ${t['amount']:.2f} - Category: {t['category']}")

def view_balance(transactions):
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = income - expenses
    print(f"\nTotal Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}")

def main():
    transactions = []
    categories = ["Food", "Rent", "Travel", "Salary", "Misc"]

    while True:
        show_menu()
        choice = get_choice()

        if choice == '1':
            add_transaction(transactions, 'income', categories)
        elif choice == '2':
            add_transaction(transactions, 'expense', categories)
        elif choice == '3':
            view_transactions(transactions)
        elif choice == '4':
            view_balance(transactions)
        elif choice == '5':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
