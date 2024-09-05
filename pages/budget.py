import streamlit as st
import pandas as pd

# Streamlit page configuration
st.set_page_config(
    page_title="Budget Planning App",
    page_icon="💸",
    layout="centered",
)

# Page title and introduction
st.title("Budget Planning App")
st.write("""
Welcome to the Budget Planning App! Use this tool to manage your income and expenses and plan your budget effectively.
""")

# Income Section
st.header("Income")
income_sources = st.text_area("Enter your income sources and amounts separated by commas (e.g., Salary, 4000, Freelance, 1500):", "")
income_list = income_sources.split(',')

# Process income input
income_dict = {}
if len(income_list) > 1 and len(income_list) % 2 == 0:
    for i in range(0, len(income_list), 2):
        source = income_list[i].strip()
        amount = float(income_list[i+1].strip())
        income_dict[source] = amount

# Expenses Section
st.header("Expenses")
expense_categories = st.text_area("Enter your expense categories and amounts separated by commas (e.g., Rent, 1200, Groceries, 300):", "")
expense_list = expense_categories.split(',')

# Process expense input
expense_dict = {}
if len(expense_list) > 1 and len(expense_list) % 2 == 0:
    for i in range(0, len(expense_list), 2):
        category = expense_list[i].strip()
        amount = float(expense_list[i+1].strip())
        expense_dict[category] = amount

# Calculation Section
st.header("Summary")

if income_dict and expense_dict:
    total_income = sum(income_dict.values())
    total_expenses = sum(expense_dict.values())
    balance = total_income - total_expenses

    st.subheader("Income Summary")
    st.write(f"Total Income: ${total_income:,.2f}")
    st.write(pd.DataFrame(list(income_dict.items()), columns=['Source', 'Amount']))

    st.subheader("Expense Summary")
    st.write(f"Total Expenses: ${total_expenses:,.2f}")
    st.write(pd.DataFrame(list(expense_dict.items()), columns=['Category', 'Amount']))

    st.subheader("Budget Balance")
    if balance >= 0:
        st.write(f"Remaining Balance: ${balance:,.2f}")
    else:
        st.write(f"Over Budget by: ${abs(balance):,.2f}")
else:
    st.write("Please enter both income and expenses to see the summary.")

# Visualization Section
if expense_dict:
    st.header("Expense Breakdown")
    expense_df = pd.DataFrame(list(expense_dict.items()), columns=['Category', 'Amount'])
    st.bar_chart(expense_df.set_index('Category'))
