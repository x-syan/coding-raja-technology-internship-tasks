import json

def main():
    transactions = load_transactions()
    while True:
        print("1. Add transaction")
        print("2. View remaining budget")
        print("3. View expense analysis")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_budget(transactions)
        elif choice == "3":
            view_expense_analysis(transactions)
        elif choice == "4":
            save_transactions(transactions)
            break
        else:
            print("Invalid choice. Please try again.")

def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": 0, "expenses": []}

def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)

def add_transaction(transactions):
    category = input("Enter transaction category: ")
    amount = float(input("Enter transaction amount: "))
    transaction_type = input("Enter transaction type (income/expense): ")
    
    if transaction_type.lower() == "income":
        transactions["income"] += amount
    elif transaction_type.lower() == "expense":
        transactions["expenses"].append({"category": category, "amount": amount})
        transactions["income"] -= amount
    else:
        print("Invalid transaction type.")

def view_budget(transactions):
    remaining_budget = transactions["income"]
    for expense in transactions["expenses"]:
        remaining_budget -= expense["amount"]
    print(f"Remaining budget: {remaining_budget}")

def view_expense_analysis(transactions):
    categories = {}
    for expense in transactions["expenses"]:
        category = expense["category"]
        if category in categories:
            categories[category] += expense["amount"]
        else:
            categories[category] = expense["amount"]
    
    print("Expense analysis:")
    for category, amount in categories.items():
        print(f"{category}: {amount}")

if __name__ == "__main__":
    main()
