class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []  
        self.expenses = []  

    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def total_income(self):
        return sum(item['amount'] for item in self.incomes)

    def total_expense(self):
        return sum(item['amount'] for item in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return (f"Account Owner: {self.firstname} {self.lastname}\n"
                f"Total Income: {self.total_income()}\n"
                f"Total Expense: {self.total_expense()}\n"
                f"Current Balance: {self.account_balance()}")

# Example Usage:
my_account = PersonAccount("Asabeneh", "Yetayeh")
my_account.add_income(5000, "Salary")
my_account.add_income(200, "Freelance")
my_account.add_expense(1500, "Rent")
my_account.add_expense(200, "Groceries")

print(my_account.account_info())
