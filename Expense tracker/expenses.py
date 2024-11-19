import os
import csv
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Ensure the CSV file exists
if not os.path.exists(EXPENSE_FILE):
    with open(EXPENSE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])

# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD, press Enter for today): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please try again.")
        return

    category = input("Enter category (e.g., Food, Transport, Utilities): ").strip()
    description = input("Enter description: ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    with open(EXPENSE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    with open(EXPENSE_FILE, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
    if len(expenses) == 1:
        print("No expenses recorded.")
        return

    print("\n--- Expenses ---")
    print(f"{'Date':<12} {'Category':<15} {'Description':<20} {'Amount':<10}")
    print("-" * 60)
    for row in expenses[1:]:
        print(f"{row[0]:<12} {row[1]:<15} {row[2]:<20} {row[3]:<10}")
    print("-" * 60)

# View total expenses by category
def category_report():
    with open(EXPENSE_FILE, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
    if len(expenses) == 1:
        print("No expenses recorded.")
        return

    category_totals = {}
    for row in expenses[1:]:
        category = row[1]
        amount = float(row[3])
        category_totals[category] = category_totals.get(category, 0) + amount

    print("\n--- Total Expenses by Category ---")
    for category, total in category_totals.items():
        print(f"{category:<15}: ${total:.2f}")
    print("-" * 30)

# View monthly expense report
def monthly_report():
    month = input("Enter month and year (MM-YYYY): ").strip()
    try:
        datetime.strptime(month, "%m-%Y")
    except ValueError:
        print("Invalid format. Please use MM-YYYY.")
        return

    with open(EXPENSE_FILE, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
    if len(expenses) == 1:
        print("No expenses recorded.")
        return

    monthly_total = 0
    print("\n--- Monthly Report ---")
    print(f"{'Date':<12} {'Category':<15} {'Description':<20} {'Amount':<10}")
    print("-" * 60)
    for row in expenses[1:]:
        if row[0].startswith(month):
            print(f"{row[0]:<12} {row[1]:<15} {row[2]:<20} {row[3]:<10}")
            monthly_total += float(row[3])

    print("-" * 60)
    print(f"Total for {month}: ${monthly_total:.2f}")

# Main menu
def main_menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses by Category")
        print("4. View Monthly Expense Report")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_report()
        elif choice == "4":
            monthly_report()
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
