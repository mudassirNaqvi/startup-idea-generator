Thank you for the clarification! Here's the updated `README.md` with the correct file name `firstapp.py`:

```markdown
# 🚀 Start-Up Idea Generator

Welcome to the **Start-Up Idea Generator**! This AI-powered tool is here to help you turn your ideas into actionable startup plans. Simply describe a problem or theme, and let AI generate a startup idea with a detailed plan, including a solution, revenue model, and target audience. 

### 🌐 Live Demo
Check out the live version of the app here:  
[Start-Up Idea Generator](https://startup-idea-generator-gmpmxs9gyaympj2xa9lvkc.streamlit.app/)

---

### Features

- **AI-Powered Startup Ideas**: Get startup ideas tailored to your problem or theme.
- **Comprehensive Startup Plans**: Includes a detailed solution, revenue model, and target audience for each idea.
- **User-Friendly Interface**: Simple and intuitive user interface to guide you through the idea generation process.

---

### Project Structure

Here's how your project folder should look:

```plaintext
startup-idea-generator/
│
├── firstapp.py              # Main app to launch the project
├── pages/
│   └── page_1.py            # Single page for user input and generated idea
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

### ⚙️ Installation Guide

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mudassirNaqvi/startup-idea-generator.git
    cd startup-idea-generator
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API Key**:
    - To use **Google Gemini API**, store your **API Key** securely. You can set it up by creating a `.env` file in the root of the project with the following content:
        ```plaintext
        GOOGLE_API_KEY="your_google_api_key_here"
        ```

4. **Run the app**:
    ```bash
    streamlit run firstapp.py
    ```

---

### 📦 Requirements

This project depends on the following libraries:

- `streamlit`
- `google-generativeai`
- Other dependencies in `requirements.txt`

---

### 🚀 How It Works

1. **Input Problem or Theme**: On the main page, users input a problem or theme they want to solve.
2. **AI-Generated Idea**: The app uses **Google Gemini AI** to generate a tailored startup idea based on the user’s input.
3. **Startup Plan**: The app displays a full startup plan, including:
    - **Problem**: The user-submitted problem.
    - **Solution**: The AI-generated solution.
    - **Revenue Model**: A suggestion for how the startup can generate revenue.
    - **Target Audience**: The suggested audience for the startup.

---

### 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 📞 Contact

Created by **[Syed Muhammad Mudassir Naqvi](https://github.com/mudassirNaqvi)**

Feel free to reach out for any queries or contributions!
