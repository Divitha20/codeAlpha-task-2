import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Define FAQ data
faq_data = {
    "What is your return policy?": "Our return policy allows returns within 30 days of purchase.",
    "How long does shipping take?": "Shipping usually takes 5-7 business days.",
    "What payment methods do you accept?": "We accept credit cards, PayPal, and bank transfers.",
    "Can I track my order?": "Yes, you can track your order using the tracking number provided in the confirmation email.",
    "What are your customer support hours?": "Our customer support is available 24/7.",
}

# Function to find the most similar FAQ question
def find_similar_question(user_input):
    user_doc = nlp(user_input)

    # Initialize variables to store the best match
    best_match = None
    best_similarity = 0.0

    # Iterate through the FAQ data to find the most similar question
    for question in faq_data:
        faq_doc = nlp(question)
        similarity = user_doc.similarity(faq_doc)

        # Update if a better match is found
        if similarity > best_similarity:
            best_match = question
            best_similarity = similarity

    return best_match

# Chatbot function to handle user input and respond with the correct FAQ
def faq_chatbot():
    print("FAQ Chatbot: Hello! How can I assist you today?")
    print("Type 'exit' to end the conversation.\n")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit the loop if the user wants to quit
        if user_input.lower() == 'exit':
            print("FAQ Chatbot: Goodbye!")
            break

        # Find the most similar FAQ question
        best_match = find_similar_question(user_input)

        if best_match:
            # Respond with the corresponding answer
            print(f"FAQ Chatbot: {faq_data[best_match]}")
        else:
            print("FAQ Chatbot: Sorry, I don't have an answer for that.")

if __name__ == "__main__":
    faq_chatbot()
