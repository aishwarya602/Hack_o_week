import datetime
import csv
from collections import Counter


class ChatbotEngine:

    def process(self, message):

        message = message.lower()

        if "hello" in message or "hi" in message:
            return "greeting", "Hello! How can I help you?"

        elif "fee" in message or "tuition" in message:
            return "fees_query", "The tuition fee is ₹50,000 per semester."

        elif "admission" in message:
            return "admission_info", "Admissions start in June."

        elif "hostel" in message:
            return "hostel_info", "Hostel facilities are available."

        else:
            return "unknown", "Sorry, I couldn't understand your query."


class Logger:

    def log(self, query, intent, response):

        with open("chat_logs.csv", "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                datetime.datetime.now(),
                query,
                intent,
                response
            ])


def chatbot_simulation():

    bot = ChatbotEngine()
    logger = Logger()

    print("\nChatbot started (type 'exit' to stop)\n")

    while True:

        query = input("You: ")

        if query.lower() == "exit":
            break

        intent, response = bot.process(query)

        print("Bot:", response)

        logger.log(query, intent, response)


def run_analytics():

    queries = []
    intents = []

    try:

        with open("chat_logs.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                queries.append(row[1])
                intents.append(row[2])

    except FileNotFoundError:

        print("No logs found yet.")
        return

    print("\n--- Analytics Report ---\n")

    query_counter = Counter(queries)
    intent_counter = Counter(intents)

    print("Top Queries:")
    for query, count in query_counter.most_common(5):
        print(query, ":", count)

    print("\nIntent Distribution:")
    for intent, count in intent_counter.items():
        print(intent, ":", count)

    unknown_queries = [
        q for q, i in zip(queries, intents) if i == "unknown"
    ]

    if unknown_queries:

        print("\nUnknown Queries Detected:")
        for q in set(unknown_queries):
            print("-", q)

        print("\nSuggested Improvements:")

        print("- Add new intents for unknown queries")
        print("- Expand keyword patterns")
        print("- Add FAQs for frequent questions")


def main():

    print("1. Run Chatbot")
    print("2. Run Analytics")

    choice = input("Choose option: ")

    if choice == "1":
        chatbot_simulation()

    elif choice == "2":
        run_analytics()

    else:
        print("Invalid choice")


main()