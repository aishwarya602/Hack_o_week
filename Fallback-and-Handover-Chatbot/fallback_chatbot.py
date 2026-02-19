# -----------------------------
# Supported Intents
# -----------------------------
supported_intents = {
    "exam": "Exams begin from March 20.",
    "fees": "The annual fee is ₹75,000.",
    "admissions": "Admissions open in June.",
    "hostel": "Hostel facilities are available for boys and girls."
}

# -----------------------------
# Detect Intent
# -----------------------------
def detect_intent(user_input):
    user_input = user_input.lower()

    for key in supported_intents:
        if key in user_input:
            return key

    return None


# -----------------------------
# Fallback Strategy
# -----------------------------
def handle_fallback():
    print("\nI'm not sure I understood your question.")
    print("You can ask about:")
    for intent in supported_intents:
        print(f"- {intent}")

    choice = input("\nWould you like to contact a human advisor? (yes/no): ").lower()

    if choice == "yes":
        print("\nPlease contact the Academic Support Desk:")
        print("📧 Email: support@institute.edu")
        print("📞 Phone: +91-9876543210")
    else:
        print("\nOkay! Please try asking your question differently.")


# -----------------------------
# Chat Loop
# -----------------------------
print("Smart FAQ Chatbot with Fallback Support")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    intent = detect_intent(user_input)

    if intent:
        print("Bot:", supported_intents[intent])
    else:
        handle_fallback()
