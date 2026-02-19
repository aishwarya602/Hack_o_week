import re

# -----------------------------
# Conversation Context
# -----------------------------
context = {
    "intent": None,
    "semester": None
}

# -----------------------------
# Helper: Extract Semester
# -----------------------------
def extract_semester(text):
    match = re.search(r"(sem|semester|year)\s*(\d+|first|second|third|fourth)", text.lower())
    
    if match:
        value = match.group(2)

        # Convert words to numbers
        mapping = {
            "first": "1",
            "second": "2",
            "third": "3",
            "fourth": "4"
        }

        return mapping.get(value, value)
    
    return None


# -----------------------------
# Intent Detection
# -----------------------------
def detect_intent(text):
    if "exam" in text.lower():
        return "exam"
    return None


# -----------------------------
# Response Generator
# -----------------------------
def generate_response(user_input):

    # Detect intent
    intent = detect_intent(user_input)
    semester = extract_semester(user_input)

    # Update context
    if intent:
        context["intent"] = intent

    if semester:
        context["semester"] = semester

    # If exam intent but no semester
    if context["intent"] == "exam" and not context["semester"]:
        return "For which semester?"

    # If we have both
    if context["intent"] == "exam" and context["semester"]:
        return f"Semester {context['semester']} exams start on March 20."

    return "Please clarify your question."


# -----------------------------
# Chat Loop
# -----------------------------
print("Context-Aware Exam Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = generate_response(user_input)
    print("Bot:", response)
