import streamlit as st

def calculate_compound_interest(principal, rate, years, compounds_per_year, deposit, deposit_frequency):
    """
    Function to calculate compound interest with regular deposits.
    
    Parameters:
    - principal (float): Initial amount of money.
    - rate (float): Annual interest rate (as a percentage).
    - years (int): Number of years the money is invested for.
    - compounds_per_year (int): Number of times the interest is compounded per year.
    - deposit (float): Regular deposit amount.
    - deposit_frequency (int): Number of deposits per year.
    
    Returns:
    - float: The amount of money accumulated after n years, including interest and deposits.
    """
    # Convert rate from percentage to a decimal
    rate_decimal = rate / 100
    # Total amount including interest
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * years)
    
    # Add regular deposits
    for i in range(1, years * deposit_frequency + 1):
        amount += deposit * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * (years - (i / deposit_frequency)))
    
    return amount

# Streamlit page title and description
st.title("Compound Interest Savings Calculator")
st.write("Calculate how much your savings will grow over time with compound interest and regular deposits.")

# Input fields for the user to enter the principal, rate, years, compounds per year, deposit amount, and deposit frequency
principal = st.number_input("Initial Principal ($):", min_value=0.0, value=1000.0)
rate = st.number_input("Annual Interest Rate (%):", min_value=0.0, value=5.0)
years = st.number_input("Number of Years:", min_value=1, value=10)
compounds_per_year = st.selectbox("Compounds per Year:", [1, 2, 4, 12])
deposit = st.number_input("Regular Deposit Amount ($):", min_value=0.0, value=100.0)
deposit_frequency = st.selectbox("Deposit Frequency per Year:", [1, 12, 26, 52])

# Calculate the compound interest live based on user input
final_amount = calculate_compound_interest(principal, rate, years, compounds_per_year, deposit, deposit_frequency)
st.write(f"After {years} years, your savings will grow to ${final_amount:,.2f}.")
