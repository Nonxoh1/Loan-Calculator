import streamlit as st
import pandas as pd

def calculate_schedule(name, loan_amount, tenure_months, annual_interest_rate):
    total_interest = loan_amount * (annual_interest_rate / 100) * (tenure_months / 12)
    total_repayment = loan_amount + total_interest

    monthly_principal = loan_amount / tenure_months
    monthly_interest = total_interest / tenure_months
    monthly_payment = monthly_principal + monthly_interest

    outstanding_balance = total_repayment
    schedule = []

    for month in range(1, tenure_months + 1):
        outstanding_balance -= monthly_payment
        if outstanding_balance < 0:
            outstanding_balance = 0.00
        schedule.append({
            "Month": month,
            "Principal (₦)": round(monthly_principal, 2),
            "Interest (₦)": round(monthly_interest, 2),
            "Monthly Payment (₦)": round(monthly_payment, 2),
            "Outstanding Balance (₦)": round(outstanding_balance, 2)
        })
    
    return total_interest, total_repayment, monthly_payment, pd.DataFrame(schedule)

# Streamlit UI
st.title("📊 Loan Calculator")

with st.form("loan_form"):
    name = st.text_input("Full Name")
    loan_amount = st.number_input("Loan Amount (₦)", min_value=0.0, step=1000.0)
    tenure_months = st.number_input("Loan Tenure (in months)", min_value=1, step=1)
    annual_interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, step=0.1)
    submit = st.form_submit_button("Calculate")

if submit:
    total_interest, total_repayment, monthly_payment, schedule_df = calculate_schedule(
        name, loan_amount, tenure_months, annual_interest_rate)

    st.subheader(f"Loan Summary for {name}")
    st.write(f"**Loan Amount:** ₦{loan_amount:,.2f}")
    st.write(f"**Total Interest:** ₦{total_interest:,.2f}")
    st.write(f"**Total Repayment:** ₦{total_repayment:,.2f}")
    st.write(f"**Tenure:** {tenure_months} months")
    st.write(f"**Monthly Payment:** ₦{monthly_payment:,.2f}")

    st.subheader("📅 Repayment Schedule")
    st.dataframe(schedule_df)
