import streamlit as st
import time

st.title("Determine a company's NAICS code")

company_url = st.text_input("Enter company's URL here:")

# Validate the URL
if company_url:
    if company_url.startswith("http://") or company_url.startswith("https://"):
        st.success(f"Valid URL: {company_url}")
        
        # Display a loading message
        with st.spinner("NAICS code loading..."):
            time.sleep(4)  # Simulate a loading process (e.g., fetching NAICS code)
        
        st.success("NAICS code determined!")
    else:
        st.error("Please enter a valid URL starting with http:// or https://")
