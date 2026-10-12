import csv
import os

f = "expenses.csv"


def init():
    if not os.path.exists(f):
        with open(f, "w", newline="") as file:
            w = csv.writer(file)
            w.writerow(["Date", "Category", "Description", "Amount"])


def add():
    d = input("Date (YYYY-MM-DD): ")
    c = input("Category: ")
    des = input("Description: ")

    while True:
        try:
            a = float(input("Amount: "))
            if a < 0:
                print("Amount must be positive.")
                continue
            break
        except:
            print("Enter a valid amount.")

    with open(f, "a", newline="") as file:
        w = csv.writer(file)
        w.writerow([d, c, des, a])

    print("Expense added.")


def report():
    total = 0
    cat = {}

    with open(f, "r") as file:
        r = csv.DictReader(file)
        for i in r:
            amt = float(i["Amount"])
            total += amt
            k = i["Category"]
            cat[k] = cat.get(k, 0) + amt

    print("\nCategory-wise Spending")
    for k, v in cat.items():
        print(k, ":", v)

    print("\nTotal Spending:", total)


def main():
    init()

    while True:
        print("\n1. Add Expense")
        print("2. View Report")
        print("3. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add()
        elif ch == "2":
            report()
        elif ch == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
