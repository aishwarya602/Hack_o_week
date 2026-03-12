# Multichannel Chatbot Deployment Mockup

## Overview

This project demonstrates a **multichannel chatbot deployment architecture** where a single chatbot backend serves multiple communication channels including:

- Web Chatbot
- Mobile Application Chatbot
- WhatsApp Chatbot

The system simulates how a chatbot would behave across different platforms while maintaining a **shared backend logic**.

This implementation uses a **console-based simulation (CLI)** to demonstrate the behavior without building actual frontend interfaces.

---

## Objectives

- Simulate chatbot deployment across multiple platforms
- Demonstrate channel-specific response formatting
- Implement a shared chatbot processing engine
- Log user interactions for future analytics

---

## System Architecture

```
User
 │
 ├── Web Chat
 ├── Mobile App
 └── WhatsApp

        ↓

Channel Handler Layer
        ↓
Chatbot Engine
        ↓
Response Formatter
        ↓
Interaction Logger
        ↓
CSV Log Storage
```

---

## Features

### 1. Multichannel Support
The chatbot simulates interaction from:
- Web users
- Mobile app users
- WhatsApp users

### 2. Unified Backend
All channels use a **single chatbot engine** to process queries.

### 3. Channel-Specific Responses

| Channel | Behavior |
|------|------|
| Web | Supports quick replies |
| Mobile | Simulates push notifications |
| WhatsApp | Uses structured reply format |

### 4. Interaction Logging
All queries and responses are stored in:

```
chat_logs.csv
```

Logged fields include:
- Timestamp
- User ID
- Channel
- Query
- Detected intent
- Response

---

## Example Queries

The chatbot can respond to questions such as:

- Hello
- What are the fees?
- Tell me about admission
- Hostel information

Unknown queries trigger a fallback response.

---

## Installation

Make sure Python is installed.

```
python --version
```

Clone or download the project.

```
git clone <repository-url>
cd multichannel-chatbot
```

---

## Running the Program

Run the chatbot simulation:

```
python multichannel_chatbot.py
```

---

## Usage

1. Select the channel:
```
web
mobile
whatsapp
```

2. Enter queries in the terminal.

Example:

```
Channel: web
You: hello
BOT: Hi! How can I assist you today?
```

Exit the chatbot by typing:

```
exit
```

---

## Example Interaction

```
Select Channel: web

You: hello
WEB BOT: Hi! How can I assist you today?

You: fees
WEB BOT: The tuition fees are ₹50,000 per semester.
[Quick Reply: Admissions | Scholarships]
```

---

## Project Structure

```
multichannel-chatbot/
│
├── multichannel_chatbot.py
├── chat_logs.csv
└── README.md
```

---

## Future Improvements

Possible enhancements include:

- Intent classification using Machine Learning
- Natural Language Processing using TF-IDF
- Integration with WhatsApp Business API
- Web UI chatbot widget
- Mobile app integration
- Real-time analytics dashboard

---

## Learning Outcomes

This project demonstrates:

- Multichannel system design
- Backend chatbot architecture
- Interaction logging for analytics
- Channel-specific response handling

---

## Author

Computer Science Engineering (AIML)

Multichannel Chatbot Deployment Mockup Project