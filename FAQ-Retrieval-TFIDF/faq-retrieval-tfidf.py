from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ Dataset
faq_questions = [
    "What are the institute timings?",
    "What is the tuition fee?",
    "How can I apply for admission?",
    "What is the contact number?",
    "Is hostel facility available?"
]

faq_answers = [
    "The institute is open from 9:00 AM to 5:00 PM, Monday to Friday.",
    "The annual tuition fee is ₹75,000.",
    "Admissions are based on entrance exam and merit.",
    "You can contact us at +91-9876543210.",
    "Hostel facilities are available for both boys and girls."
]

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Convert FAQ questions into TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(faq_questions)

print("Welcome to FAQ Retrieval Chatbot (TF-IDF Based)")
print("Type 'exit' to quit.\n")

while True:
    user_query = input("Enter your question: ")

    if user_query.lower() == "exit":
        print("Goodbye!")
        break

    # Transform user query
    user_vector = vectorizer.transform([user_query])

    # Compute cosine similarity
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)

    # Get index of best match
    best_match_index = similarity_scores.argmax()

    print("\nBot:", faq_answers[best_match_index])
    print()
