## 🤖 Customer Support Chatbot (NLTK & spaCy)

This project is a basic customer support chatbot built using Natural Language Processing (NLP) concepts in Python.
It demonstrates how to preprocess text, extract keywords, and generate responses using NLTK and an improved version using spaCy.
This project is beginner-friendly and suitable for students, internships, and NLP fundamentals practice.

## 📌 Features

Text preprocessing (tokenization, stopword removal, lemmatization)
Rule-based response system
Supports common customer queries:
Greeting
Working hours
Contact details
Office location
Refund policy
Improved accuracy using spaCy
Simple command-line chatbot

## 🧠 Technologies Used

    Python
    spaCy

## 📂 Project Structure
nltk-chatbot/

├── step7_spacy_customer_chatbot.py        # spaCy-based improved chatbot
├── requirements.txt
└── README.md

## ⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/saeenikam19/ChatBot_using_SpaCy.git

2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows

📦 Install Required Libraries
pip install -r requirements.txt

Download spaCy English model
python -m spacy download en_core_web_sm

▶️ How to Run the Chatbot

Run spaCy-based chatbot (recommended)
python step7_spacy_customer_chatbot.py

## 💬 Example Interaction
ChatBot: Hello! Ask me a question (type 'exit' to quit)
You: What are your working hours?
ChatBot: Our working hours are 9 AM to 6 PM, Monday to Friday.

## 🚀 Learning Outcomes

Understanding NLP preprocessing steps

Difference between NLTK vs spaCy

Building a rule-based chatbot

Improving chatbot accuracy using lemmatization

Structuring a Python NLP project for GitHub
