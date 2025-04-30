import streamlit as st
import google.generativeai as genai


st.set_page_config(page_title="Idea Generator", layout="wide")
st.title(":bulb: Describe Your Idea or Problem")

user_input = st.text_area("What problem are you trying to solve?", height=150)

if st.button("Generate Startup Plan"):
    if user_input.strip() == "":
        st.warning("Please enter a problem or theme first.")
    else:
        st.success("Here's your AI-generated startup idea:")
        st.write(f"**Problem:** {user_input}")

        
        client = genai.Client(api_key="AIzaSyAe8PzE8U2nNv9rEUq4d0XLGFTnkHeYMHY")

        response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"""
        You are an AI model strictly limited to generating startup ideas only.
        If the user asks anything outside startup ideas, respond with:
        'Sorry, I can only help you come up with startup ideas.'

        Now respond to the following prompt accordingly:
        {user_input}
        """
        )

        st.markdown(f"**Solution:** {response.text}")
        st.markdown("**Revenue Model:** Freemium + Subscription for expert access.")
        st.markdown("**Target Audience:** Startups, students, professionals, and innovators.")

placeholder_footer = st.empty()

with placeholder_footer.container():
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; font-size: 14px;'>"
        "Created by <b>Syed Muhammad Mudassir Naqvi</b></p>",
        unsafe_allow_html=True
    )
