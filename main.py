import streamlit as st

# Streamlit page configuration
st.set_page_config(
    page_title="Financial Tools Hub",
    page_icon="💰",
    layout="centered",
)

# Page title and introduction
st.title("Welcome to Your Financial Tools Hub")
st.write("""
Explore a variety of tools and resources to help you manage your finances more effectively. Whether you're planning for the future, looking to invest, or just curious about how your money can grow, our suite of calculators and resources are here to assist you every step of the way.
""")

# Compound Interest Calculator Section
st.subheader("🔄 Compound Interest Calculator")
st.write("""
Discover how your savings can grow over time with the power of compound interest. Use our calculator to see the impact of different interest rates, time periods, and compounding frequencies on your initial investment.
""")

# Financial Help Section
st.subheader("📊 Further Financial Help and Tools")
st.write("""
Our financial help section offers a range of tools and resources designed to provide guidance on a variety of topics:
- **Budgeting Tools:** Create and manage your personal or household budget.
- **Retirement Planning:** Estimate how much you need to save for a comfortable retirement.
- **Loan Calculators:** Understand the costs associated with different types of loans and find the best options for you.
- **Investment Advice:** Learn about different investment options and strategies to maximize your returns.
""")


# Footer
st.write("---")
st.write("© 2024 Your Financial Tools Hub. All rights reserved.")
