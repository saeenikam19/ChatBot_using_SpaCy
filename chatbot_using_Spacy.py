import spacy

nlp = spacy.load("en_core_web_sm")

responses = {
    "hello": "Hello! How can I help you?",
    "hour": "Our working hours are 9 AM to 6 PM, Monday to Friday.",
    "contact": "You can contact us at support@example.com.",
    "location": "Our office is located in Pune, India.",
    "refund": "Yes, we provide refunds within 7 days of purchase."
}

def get_keywords(text):
    doc = nlp(text.lower())
    keywords = []

    for token in doc:
        if token.is_alpha and not token.is_stop:
            keywords.append(token.lemma_)

    return keywords

def get_response(user_input):
    keywords = get_keywords(user_input)

    for word in keywords:
        if word in responses:
            return responses[word]

    return "Sorry, I did not understand your question."

print("ChatBot: Hello! Ask me a question (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("ChatBot: Thank you! Have a great day 😊")
        break

    print("ChatBot:", get_response(user_input))
