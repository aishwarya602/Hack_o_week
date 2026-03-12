import datetime
import csv


class ChatbotEngine:

    def process(self, message):

        message = message.lower()

        if "hello" in message or "hi" in message:
            return "greeting", "Hi! How can I assist you today?"

        elif "fee" in message or "tuition" in message:
            return "fees_query", "The tuition fees are ₹50,000 per semester."

        elif "admission" in message:
            return "admission_info", "Admissions start in June every year."

        elif "hostel" in message:
            return "hostel_info", "Hostel facilities are available for students."

        else:
            return "unknown", "Sorry, I couldn't understand your query."


class Logger:

    def log(self, user_id, channel, query, intent, response):

        with open("chat_logs.csv", "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                datetime.datetime.now(),
                user_id,
                channel,
                query,
                intent,
                response
            ])


class ChannelHandler:

    def __init__(self, channel):

        self.channel = channel
        self.bot = ChatbotEngine()

    def format_response(self, response):

        if self.channel == "web":

            return f"{response}\n[Quick Reply: Admissions | Scholarships]"

        elif self.channel == "mobile":

            return f"{response}\n(Push Notification Sent)"

        elif self.channel == "whatsapp":

            return f"{response}\nReply with:\n1 - Fees\n2 - Admissions"

        else:
            return response

    def handle_message(self, message):

        intent, response = self.bot.process(message)

        formatted = self.format_response(response)

        return intent, formatted


def simulate():

    logger = Logger()

    print("Choose Channel: web / mobile / whatsapp")
    channel = input("Channel: ").lower()

    handler = ChannelHandler(channel)

    user_id = "student_001"

    print("\nType 'exit' to quit\n")

    while True:

        query = input("You: ")

        if query.lower() == "exit":
            break

        intent, response = handler.handle_message(query)

        print(f"{channel.upper()} BOT:", response)

        logger.log(user_id, channel, query, intent, response)


simulate()