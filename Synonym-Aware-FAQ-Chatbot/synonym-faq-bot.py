# Synonym-Aware FAQ Bot

# Dictionary with keyword groups (synonyms)
faq_data = {
    "timing": {
        "keywords": ["timing", "time", "hours", "schedule"],
        "response": "The institute is open from 9:00 AM to 5:00 PM, Monday to Friday."
    },
    "fees": {
        "keywords": ["fees", "fee", "tuition", "payment", "cost"],
        "response": "The annual tuition fee is ₹75,000."
    },
    "admission": {
        "keywords": ["admission", "enrollment", "apply", "registration"],
        "response": "Admissions are based on entrance exam and merit."
    },
    "contact": {
        "keywords": ["contact", "phone", "email", "call"],
        "response": "You can contact us at +91-9876543210 or email info@institute.edu."
    },
    "hostel": {
        "keywords": ["hostel", "accommodation", "stay", "dorm"],
        "response": "Hostel facilities are available for both boys and girls."
    }
}

print("Welcome to Synonym-Aware FAQ Chatbot!")

while True:

    print("\nYou can ask about: timing, fees, admission, contact, hostel")
    user_input = input("Enter your query keyword: ").lower()

    found = False

    for category in faq_data:
        if user_input in faq_data[category]["keywords"]:
            print("Bot:", faq_data[category]["response"])
            found = True
            break

    if not found:
        print("Bot: Please contact the institute for more information.")

    choice = input("\nWould you like to know more? (yes/no): ").lower()

    if choice == "no":
        print("Bot: Thank you! Goodbye.")
        break
