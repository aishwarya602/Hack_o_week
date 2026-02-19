from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# -----------------------------
# Training Data
# -----------------------------

training_sentences = [
    # Admissions
    "How can I apply for admission?",
    "What is the admission process?",
    "When do admissions start?",
    
    # Exams
    "When are the exams scheduled?",
    "What is the exam syllabus?",
    "How many exams are there?",
    
    # Timetable
    "What is today's timetable?",
    "When are the classes?",
    "Show me the class schedule.",
    
    # Hostel
    "Is hostel facility available?",
    "What are hostel charges?",
    "How to apply for hostel?",
    
    # Scholarships
    "Are scholarships available?",
    "How can I apply for scholarship?",
    "What are scholarship criteria?",
    
    # Fees
    "What is the tuition fee?",
    "How much are the fees?",
    "When should I pay the fees?",
    
    # Placements
    "What is the placement record?",
    "What companies visit for placements?",
    "What is the average package?"
]

training_labels = [
    "admissions", "admissions", "admissions",
    "exams", "exams", "exams",
    "timetable", "timetable", "timetable",
    "hostel", "hostel", "hostel",
    "scholarships", "scholarships", "scholarships",
    "fees", "fees", "fees",
    "placements", "placements", "placements"
]

# -----------------------------
# Build Model Pipeline
# -----------------------------

model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# Train model
model.fit(training_sentences, training_labels)

print("Student Intent Classification System")
print("Type 'exit' to quit.\n")

# -----------------------------
# Prediction Loop
# -----------------------------

while True:
    query = input("Enter your query: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    predicted_intent = model.predict([query])[0]

    print("Predicted Intent:", predicted_intent)
    print()
