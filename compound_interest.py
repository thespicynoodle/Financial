import streamlit as st

def calculate_compound_interest(principal, rate, years, compounds_per_year):
    """
    Function to calculate compound interest.
    
    Parameters:
    - principal (float): Initial amount of money.
    - rate (float): Annual interest rate (as a percentage).
    - years (int): Number of years the money is invested for.
    - compounds_per_year (int): Number of times the interest is compounded per year.
    
    Returns:
    - float: The amount of money accumulated after n years, including interest.
    """
    # Convert rate from percentage to a decimal
    rate_decimal = rate / 100
    # Compound interest formula
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * years)
    return amount

# Streamlit page title and description
st.title("Compound Interest Savings Calculator")
st.write("Calculate how much your savings will grow over time with compound interest.")

# Input fields for the user to enter the principal, rate, years, and compounds per year
principal = st.number_input("Initial Principal ($):", min_value=0.0, value=1000.0)
rate = st.number_input("Annual Interest Rate (%):", min_value=0.0, value=5.0)
years = st.number_input("Number of Years:", min_value=1, value=10)
compounds_per_year = st.selectbox("Compounds per Year:", [1, 2, 4, 12])

# Calculate the compound interest based on user input
if st.button("Calculate"):
    final_amount = calculate_compound_interest(principal, rate, years, compounds_per_year)
    st.write(f"After {years} years, your savings will grow to ${final_amount:,.2f}.")
