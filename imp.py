# Import the module
import streamlit as st 

# Define the EMI caculation function
def calculate_emi(p, n, r):

	# Apply the formula
	emi = p * (r/100) * (1 + r/100)**n / ((1+r/100)**n -1)

	# Write the EMI calculated on screen
	st.write("EMI Calculated: ", round(emi,3))

# Define the Outstanding Loan Balance caculation function
def calculate_outstanding_balance(p, n, r, m):

	# Apply the formula
	balance = (p * ((1+r/100)**n - (1+r/100)**m) )/ ((1+r/100)**n - 1)

	# Write the Outstanding Loan Balance calculated on screen
	st.write("Outstanding Loan Balance Calculated: ", round(balance,3))	

# Add the title to the app
st.title("EMI Calculator")      

# Take the inputs from user
principal = st.slider("Loan Amount", 1000.0, 100000.0)
tenure = st.slider("Tenure in years", 1, 30)
roi = st.slider("Interest Rate (% P.A.)", 1, 15)
period = st.slider("Period after to check Outstanding Loan Balance in months", 1, tenure * 12)

# principal = 50000
# tenure = 2
# roi = 5.05
# period = 4

# Calculate the 'n' and 'r' values
n = tenure * 12
r = roi / 12

emi_button = st.button("Calculate EMI")
balance_button = st.button("Calculate Outstanding Loan Balance")

# Create the button and event to calculate EMI
if emi_button:
	calculate_emi(principal, n, r)

elif balance_button:
	calculate_outstanding_balance(principal, n, r, period)
