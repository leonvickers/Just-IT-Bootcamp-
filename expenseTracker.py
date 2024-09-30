expenses = []
expense1 = {'Amount': '51.00', 'category': 'shirt'}
expenses.append(expense1)
expense2 = {'Amount': '21.55', 'category': 'Food'}
expenses.append(expense2)
#Functions for expense tracker
def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break
        except:
            print("invalid input. Please try again")

def addExpense(amount, category):
    expense = {'Amount': amount, 'category': category}
    expenses.append(expense)

def printMenu():
    print("please choose from one of the following options...")
    print("1. Add a new expense")
    print("2. Remove an expense")
    print("3. List all expenses")

def listExpenses():
    print("\nHere is a list of your expenses...")
    print("---------")
    counter = 0
    for expense in expenses:
        print("#", counter, " - ", expense['Amount'], " - ", expense['category'])
        counter += 1
    print("\n\n")

if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if optionSelected == "1":
            print("How much was the expense?")
            while True:
                try:
                    amountToAdd = input("> ")
                    break
                except:
                    print("invalid input. Please try again")

            print("What category was this expense?")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                    print("invalid input. Please try again")
            addExpense(amountToAdd, category)
        elif optionSelected == "2":
            removeExpense()
        elif optionSelected == "3":
            listExpenses()
        else:
            print("invalid input. Please try again")

            