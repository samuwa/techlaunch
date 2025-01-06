import streamlit as st
import numpy_financial as npf

st.set_page_config(page_title="Mortgage Calculator", layout="wide")

st.subheader("Mortgage Payment Calculator")

col1, col2, col3 = st.columns([7,1,2])
col1.write("One of the first classes business students take is :blue[Financial Accounting], where they learn about loans and interest rates.")
col1.write("Impress the admissions committee and get a head start in your business career building your own :green[Mortgage Calculator!]")

popover = col3.popover("What is a mortgage? 	:thinking_face:")
popover.info("A mortgage is a **loan backed by a real state asset**, usually given by a bank to someone buying a home. Like many other loans,"
             "mortgages have an *interest rate* and are usually payed monthly by the *lendee*.")

st.markdown("#")

col1, col2, col3 = st.columns([5,1,5])

with col1:
    with st.form("Inputs"):
        st.write("**:red[Calculator]**")
        loan_amount = st.number_input("Loan Amount ($)", min_value=10000, max_value=1000000, value=150000, step=10000)
        interest_rate = st.slider("Interest Rate (%)", min_value=0.1, max_value=10.0, value=3.5, step=0.1)
        loan_years = st.selectbox("Loan Term (years)", options=[10, 15, 20, 30], index=3)
        submit = st.form_submit_button("Calculate Payments!")

        if submit:

            monthly_interest_rate = interest_rate / 100 / 12
            number_of_payments = loan_years * 12
            mortgage_payment = npf.pmt(monthly_interest_rate, number_of_payments, -loan_amount)

            st.success(f"Monthly Payment: ${mortgage_payment:,.2f}")

col3.latex(r"""
PMT = P \frac{r(1+r)^n}{(1+r)^n-1}
""")
col3.write("Where:")
col3.markdown("""
- \( PMT \) is the fixed monthly payment
- \( P \) is the loan amount (principal)
- \( r \) is the monthly interest rate
- \( n \) is the number of payments (term)
""")


col3.divider()
col3.write("**:red[Python]** Function for Mortgage Calculation")
code = """
import numpy_financial as npf

def calculate_mortgage(P, r, n):
    monthly_interest_rate = r / 100 / 12
    number_of_payments = n * 12
    return npf.pmt(monthly_interest_rate, number_of_payments, -P)
"""
col3.code(code, language='python')

col3.warning('''**You have never seen this before?** 
                :green[Perfect!] We will learn every part of it.''')

