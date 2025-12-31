expenses = []
expense1 = {'amount': '51.00', 'category': 'shirt'}
expenses.append(expense1)
expense2 = {'amount': '21.55', 'category': 'food'}
expenses.append(expense2)
#Functions for expense tracker
def remove_expense():
    while True:
        list_expenses()
        print("What expense would you like to remove?")
        try:
            expense_to_remove = int(input("> "))
            del expenses[expense_to_remove]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please try again")

def add_expense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def print_menu():
    print("please choose from one of the following options...")
    print("1. Add a new expense")
    print("2. Remove an expense")
    print("3. List all expenses")

def list_expenses():
    print("\nHere is a list of your expenses...")
    print("---------")
    counter = 0
    for expense in expenses:
        print("#", counter, " - ", expense['amount'], " - ", expense['category'])
        counter += 1
    print("\n\n")

if __name__ == "__main__":
    while True:
        print_menu()
        optionSelected = input("> ")

        if optionSelected == "1":
            print("How much was the expense?")
            while True:
                try:
                    amountToAdd = float(input("> "))
                    if amountToAdd <= 0:
                        raise ValueError("Amount must be positive")
                    break
                except ValueError:
                    print("Invalid input. Please enter a positive number")

            print("What category was this expense?")
            while True:
                try:
                    category = input("> ")
                    if category.strip():
                        break
                    else:
                        raise ValueError("Category cannot be empty")
                except ValueError:
                    print("Invalid input. Please enter a category")
            add_expense(amountToAdd, category)
        elif optionSelected == "2":
            remove_expense()
        elif optionSelected == "3":
            list_expenses()
        else:
            print("invalid input. Please try again")

            