import streamlit as st
import time

st.title("Find your NAICS Code")

company_url = st.text_input("Enter your company's URL here:")

# Validate the URL
if company_url:
    if company_url.startswith("http://") or company_url.startswith("https://"):
        st.success(f"Valid URL: {company_url}")
        
        # Display a loading message
        with st.spinner("NAICS code loading..."):
            time.sleep(2)  # Simulate a loading process (e.g., fetching NAICS code)
        
        st.success("NAICS code loaded!")
    else:
        st.error("Please enter a valid URL starting with http:// or https://")
