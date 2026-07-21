import streamlit as st
st.title("SIP Calculator")
monthly_sip= st.number_input("Enter Monthly Sip amount", min_value=0.0)
years=st.number_input("Enter investment period(year)",min_value=0.1, step=0.1)python
expected_return= st.number_input("Enter expected annual return (%):", min_value=0.0)
if st.button("Calculate"):
 months= int(years*12)
monthly_rate= expected_return/12/100
future_value= monthly_sip *(((1+monthly_rate)** months -1)/monthly_rate)*(1+monthly_rate)
total_investment = monthly_sip * months
profit = future_value-total_investment
st.subheader("\n------- SIP Result-------")
st.write(f"Total Investment: INR(round(total_investment):,)")
st.write(f"Futue value: INR (round(future_value):,)")
st.write(f"Estimated Profit: INR (round(profit):,)")