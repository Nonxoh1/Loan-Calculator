def calculate_simple_interest_schedule():
    print("==== Loan Calculator ====\n")
    name = input("Full Name: ")
    loan_amount = float(input("Loan Amount (₦): "))
    tenure_months = int(input("Loan Tenure (in months): "))
    annual_interest_rate = float(input("Annual Interest Rate (%): "))

    # Simple interest = P * R * T
    total_interest = loan_amount * (annual_interest_rate / 100) * (tenure_months / 12)
    total_repayment = loan_amount + total_interest

    monthly_principal = loan_amount / tenure_months
    monthly_interest = total_interest / tenure_months
    monthly_payment = monthly_principal + monthly_interest

    outstanding_balance = total_repayment
    schedule = []

    print(f"\nLoan Summary for {name}")
    print(f"Loan Amount: ₦{loan_amount:,.2f}")
    print(f"Total Interest: ₦{total_interest:,.2f}")
    print(f"Total Repayment: ₦{total_repayment:,.2f}")
    print(f"Tenure: {tenure_months} months")
    print(f"Monthly Payment: ₦{monthly_payment:,.2f}")

    print("\nRepayment Schedule:")
    print(f"{'Month':<6} {'Principal':>12} {'Interest':>12} {'Monthly Payment':>18} {'Outstanding Balance':>22}")

    for month in range(1, tenure_months + 1):
        outstanding_balance -= monthly_payment
        if outstanding_balance < 0:
            outstanding_balance = 0.00
        schedule.append({
            "Month": month,
            "Principal": round(monthly_principal, 2),
            "Interest": round(monthly_interest, 2),
            "Monthly Payment": round(monthly_payment, 2),
            "Outstanding Balance": round(outstanding_balance, 2)
        })
        print(f"{month:<6} {monthly_principal:>12,.2f} {monthly_interest:>12,.2f} "
              f"{monthly_payment:>18,.2f} {outstanding_balance:>22,.2f}")


# Run the script
calculate_simple_interest_schedule()
