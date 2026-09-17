# 🤖 LangChain AI Chatbot

An AI-powered chatbot built with **LangChain**, **Groq**, and **Streamlit**. This chatbot maintains conversation history, supports configurable AI responses, and includes a built-in calculator tool.

---

## ✨ Features

- 💬 Conversational AI using LangChain
- ⚡ Ultra-fast responses powered by Groq LLM
- 🧠 Conversation memory
- 🧮 Built-in calculator tool
- 🎛️ Adjustable temperature slider
- 🗑️ Clear chat functionality
- 🎨 Clean Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- LangChain Groq
- Groq API
- dotenv

---

## 📂 Project Structure

```
LangChain-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/LangChain-AI-Chatbot.git

cd LangChain-AI-Chatbot
```

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

Create a file named

```
.env
```

Add your Groq API key

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📦 Requirements

Example `requirements.txt`

```text
streamlit
python-dotenv
langchain
langchain-core
langchain-groq
```

Install using

```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works

1. User enters a prompt.
2. LangChain builds the prompt.
3. Conversation history is loaded.
4. Prompt is sent to Groq's Llama model.
5. AI generates a response.
6. Memory is updated for future conversations.
7. If the prompt starts with **calculate**, the calculator tool is used instead of the LLM.

---

## 💡 Example Prompts

```
What is Artificial Intelligence?

Explain Python decorators.

Write a professional email.

Summarize this paragraph.

calculate 45*23

calculate (56+89)/3
```

---


## 🔒 Environment Variables

| Variable | Description |
|----------|-------------|
| GROQ_API_KEY | Your Groq API Key |

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Nekkanti Jahnavi**

Computer Science Engineering Student

GitHub: https://github.com/your-username

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

Happy Coding! 🚀