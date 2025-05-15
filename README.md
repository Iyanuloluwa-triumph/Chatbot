# 🧠 Fake Chatbot

This is a simple fake chatbot project built with Python. It simulates a conversation by responding to user inputs using predefined logic.

---

## 📁 Project Structure

chatbot/
├── chatbot.py
├── wikipedia.py
├── weather.py
├── dict.py
├── cores.py
├── requirements.txt
└── ...

---

## 🔍 Logic

- Uses the `requests` module to access data from the internet using a customized API key.
- Uses the `pipreqs` module to generate a `requirements.txt` file based on imported libraries (for collaboration and deployment).
- Accesses data from integrated modules using **static methods** that call **class instances** in the main script.
- Will include a `pytest` test suite soon to validate functionality.
- Retrieves summaries from Wikipedia based on user input using the `wikipedia` library.

---

## 🚀 Features

- 📚 Scrapes and summarizes web data from Wikipedia to explain or define user-requested topics.
- 🌤️ Pulls real-time weather data using the OpenWeatherMap API.
- 💬 Basic chatbot responses simulate natural conversations.
- 💡 Offers motivational quotes tailored to user moods or keywords.

---

## ✅ How to Run

1. Make sure all files are in the same folder.
2. Install dependencies (generated with pipreqs):

```bash
pip install -r requirements.txt
Run the main chatbot script:

bash
python chatbot.py
🔧 Coming Soon
🧪 Unit testing using pytest

🌐 GUI implementation using Tkinter or PyQt

🤖 Smarter response engine with NLP libraries like NLTK or spaCy

📄 License
MIT License


---

---


