import streamlit as st



st.set_page_config(page_title="Start-Up Idea Generator", layout="wide")
st.title(":blue[_Start-Up Idea_] _Generator_")
st.header(":blue[_Welcome to Start-Up Idea Generator — your AI-powered innovation assistant, built in collaboration with the National Incubation Center_]" ,divider=True)
st.markdown("***Have an idea? A problem to solve? Or maybe just a passion for innovation? This app helps you turn those sparks into full-fledged startup plans using advanced generative AI.***")

multi = '''🔍 ***Describe a problem or theme***

✨ ***Let our AI generate a startup plan for you***

📈 ***Explore your idea’s potential in minutes***'''

st.markdown(multi, unsafe_allow_html=True)
st.page_link("pages/page_1.py", label=":blue[_Get Started_]",icon="➡️")

placeholder_footer = st.empty()

with placeholder_footer.container():
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; font-size: 14px;'>"
        "Created by <b>Syed Muhammad Mudassir Naqvi</b></p>",
        unsafe_allow_html=True
    )
