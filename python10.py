from datetime import datetime

FILENAME = "expenses.txt"


class Expense:
    def __init__(self, amount, category, date_time):
        self.amount = amount
        self.category = category
        self.date_time = date_time

    def to_string(self):
        return f"{self.amount}|{self.category}|{self.date_time}\n"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(FILENAME, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        amount, category, date_time = parts
                        self.expenses.append(
                            Expense(int(amount), category, date_time)
                        )
        except FileNotFoundError:
            pass

    def save_expenses(self):
        with open(FILENAME, "w") as f:
            for exp in self.expenses:
                f.write(exp.to_string())

    def get_valid_amount(self):
        while True:
            try:
                return int(input("Enter amount: "))
            except ValueError:
                print("Enter numbers only")

    def add_expense(self):
        amount = self.get_valid_amount()
        category = input("Enter category: ")
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.expenses.append(Expense(amount, category, date_time))
        self.save_expenses()
        print("Expense added")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found")
            return

        print("\n--- Expenses ---")
        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. ₹{exp.amount} | {exp.category} | {exp.date_time}")

    def delete_expense(self):
        self.view_expenses()
        if not self.expenses:
            return

        try:
            choice = int(input("Enter number to delete: "))
            self.expenses.pop(choice - 1)
            self.save_expenses()
            print("Expense deleted")
        except (ValueError, IndexError):
            print("Invalid choice")

    def category_total(self):
        totals = {}
        for exp in self.expenses:
            totals[exp.category] = totals.get(exp.category, 0) + exp.amount

        print("\n--- Category Totals ---")
        for cat, amt in totals.items():
            print(f"{cat}: ₹{amt}")

    def menu(self):
        while True:
            print("\n1.Add Expense")
            print("2.View Expenses")
            print("3.Delete Expense")
            print("4.Category Total")
            print("5.Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.delete_expense()
            elif choice == "4":
                self.category_total()
            elif choice == "5":
                print("Bye RK")
                break
            else:
                print("Invalid option")


tracker = ExpenseTracker()
tracker.menu()