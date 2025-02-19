import streamlit as st
import pandas as pd

# Load the mock data set
df = pd.read_csv('subscriptions.csv')

# Title of the app
st.title("Subscription Tracker")

# Display the data in the app
st.header("Current Subscriptions")
st.dataframe(df)

# Sidebar for adding new subscriptions
st.sidebar.header("Add a New Subscription")
new_subscription = st.sidebar.text_input("Subscription Name")
new_start_date = st.sidebar.date_input("Start Date")
new_renewal_period = st.sidebar.number_input("Renewal Period (days)", min_value=1, step=1)
new_cost = st.sidebar.number_input("Cost ($)", min_value=0.0, step=0.01)

if st.sidebar.button("Add Subscription"):
    new_data = {
        'Subscription': [new_subscription],
        'Start_Date': [new_start_date],
        'Renewal_Period': [new_renewal_period],
        'Cost': [new_cost]
    }
    new_df = pd.DataFrame(new_data)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv('subscriptions.csv', index=False)
    st.success("Subscription added!")
    st.dataframe(df)
    