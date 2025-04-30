
# 💡 Startup Idea Generator (Powered by Gemini)

This is a Streamlit web app that uses Google's Gemini AI model to help users generate unique **startup ideas** based on their input topics or interests. The app is strictly limited to startup idea generation and will reject any unrelated queries.

---

## 🚀 Demo

Try it live: [Streamlit App Link](https://your-app-name.streamlit.app/)  
GitHub Repo: [GitHub Repository](https://github.com/yourusername/startup-idea-generator)

---

## 📌 Features

- ✅ Uses **Google Gemini 1.5 Flash** for fast and creative idea generation
- ✅ Simple and clean Streamlit UI
- ✅ Rejects non-startup-related queries with a polite message
- ✅ Easy to deploy on [Streamlit Community Cloud](https://streamlit.io/cloud)

---

## 📥 Installation

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/startup-idea-generator.git
cd startup-idea-generator
```

### Step 2: Install Dependencies

Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Your Gemini API Key

You need a [Gemini API key](https://aistudio.google.com/app/apikey) to make the app work. Once you have your key, replace the placeholder in `app.py`:

```python
configure(api_key="YOUR_GEMINI_API_KEY")
```

### Step 4: Run the App

Start the app locally using Streamlit:

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. The app takes a **topic** (e.g., "healthcare", "AI for education") from the user.
2. It sends the input to the Gemini model with instructions to **only generate startup ideas**.
3. If the input is unrelated to startup ideas, Gemini will reply with:
   > "Sorry, I can only help you come up with startup ideas."

---

## 🧑‍💻 Code Overview

### `app.py`

```python
import streamlit as st
from google.generativeai import GenerativeModel, configure

# Configure Gemini API (replace with your API key)
configure(api_key="YOUR_GEMINI_API_KEY")

model = GenerativeModel("gemini-1.5-flash")

# Streamlit app setup
st.title("💡 Startup Idea Generator")
st.markdown("""
> ⚠️ **Note:** This AI model is strictly designed **only** for generating startup ideas.  
> Please enter a topic or industry (e.g., "healthcare", "AI for education").
""")

# User input field
user_input = st.text_input("Enter your topic of interest:")

# Generating the idea when user input is provided
if user_input:
    prompt = f"""
    You are an AI model strictly limited to generating startup ideas only.
    If the user asks anything outside startup ideas, respond with:
    'Sorry, I can only help you come up with startup ideas.'

    Now respond to the following prompt accordingly:
    {user_input}
    """
    response = model.generate_content(prompt)
    st.write(response.text)
```

### `requirements.txt`

```txt
streamlit
google-generativeai
```

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://aistudio.google.com/app/)
- Python 3.8+

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙋‍♂️ Author

**Syed Muhammad Mudassir Naqvi**  
[LinkedIn](https://www.linkedin.com/in/syedmudassirnaqvi) · [GitHub](https://github.com/yourusername)
```

---

### 📂 Folder Structure

Here is how your project folder should look:

```
startup-idea-generator/
│
├── app.py                     # Main Streamlit app file
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── pages/                     # Subdirectory for additional Streamlit pages
    └── page_1.py              # Startup Idea Generator page


---

### ✅ GitHub Repo Setup

1. **Go to GitHub**: [GitHub](https://github.com)  
2. **Create a new repository**: Name it `startup-idea-generator`.
3. **Push your code to GitHub**: 

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/startup-idea-generator.git
git push -u origin main
```

---

### 📥 Streamlit Cloud Hosting

1. **Go to [Streamlit Cloud](https://streamlit.io/cloud)** and sign in with your GitHub account.
2. **Click "New app"**, select your GitHub repository (`startup-idea-generator`), and deploy the app.
3. **Share your app's link** once deployed: `https://your-app-name.streamlit.app/`

