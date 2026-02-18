# FAQ Chatbot

faq_responses = {
    "timing": "The institute is open from 9:00 AM to 5:00 PM, Monday to Friday.",
    "fees": "The annual tuition fee is ₹3,00,000.",
    "admission": "Admissions are based on entrance exam and merit.",
    "contact": "You can contact us at +91-1234567890 or email info@institute.edu.",
    "location": "We are located in Nagpur, Maharashtra.",
    "hostel": "Hostel facilities are available for both boys and girls.",
    "library": "The library is open from 8:00 AM to 9:00 PM.",
    "courses": "We offer B.Tech, M.Tech, and MBA programs.",
    "placements": "Our average placement package is ₹6 LPA.",
    "internship": "Internship assistance is provided in 3rd and 4th year."
}

print("Welcome to Institute FAQ Chatbot!")

while True:

    print("\nYou can ask about the following topics:")
    for key in faq_responses:
        print("-", key)

    user_input = input("\nEnter your question keyword: ").lower()

    if user_input in faq_responses:
        print("Bot:", faq_responses[user_input])
    else:
        print("Bot: Please contact the institute for more information.")

    # Ask if user wants to continue
    choice = input("\nWould you like to know more? (yes/no): ").lower()

    if choice == "no":
        print("Bot: Thank you for using the FAQ chatbot. Goodbye!")
        break
    elif choice != "yes":
        print("Bot: Invalid choice. Exiting for safety.")
        break
