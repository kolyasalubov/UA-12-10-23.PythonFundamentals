import tkinter as tk
from tkinter import ttk
from datetime import datetime


class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.notebook = ttk.Notebook(root)
        self.add_expense_tab()
        self.report_tab()

    def add_expense_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Add Expense')

        label_category = tk.Label(tab, text='Category:')
        label_category.grid(row=0, column=0, padx=10, pady=10)

        self.entry_category = tk.Entry(tab)
        self.entry_category.grid(row=0, column=1, padx=10, pady=10)

        label_amount = tk.Label(tab, text='Amount:')
        label_amount.grid(row=1, column=0, padx=10, pady=10)

        self.entry_amount = tk.Entry(tab)
        self.entry_amount.grid(row=1, column=1, padx=10, pady=10)

        label_description = tk.Label(tab, text='Description:')
        label_description.grid(row=2, column=0, padx=10, pady=10)

        self.entry_description = tk.Entry(tab)
        self.entry_description.grid(row=2, column=1, padx=10, pady=10)

        btn_add_expense = tk.Button(tab, text='Add Expense', command=self.add_expense)
        btn_add_expense.grid(row=3, column=0, columnspan=2, pady=10)

    def report_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Expense Report')

        self.text_report = tk.Text(tab, height=10, width=40)
        self.text_report.grid(row=0, column=0, padx=10, pady=10)

        btn_generate_report = tk.Button(tab, text='Generate Report', command=self.generate_report)
        btn_generate_report.grid(row=1, column=0, pady=10)

    def add_expense(self):
        category = self.entry_category.get()
        amount = float(self.entry_amount.get())
        description = self.entry_description.get()

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        expense = f"Category: {category} | Amount: {amount} | Description: {description} | Time: {timestamp}"

        with open('expenses.txt', 'a') as file:
            file.write(expense + '\n')

        self.entry_category.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)

    def generate_report(self):
        with open('expenses.txt', 'r') as file:
            expenses = file.readlines()

        report = "Expense Report:\n\n"
        for expense in expenses:
            report += expense

        self.text_report.delete(1.0, tk.END)
        self.text_report.insert(tk.END, report)


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    app.notebook.pack(expand=1, fill='both')
    root.mainloop()
