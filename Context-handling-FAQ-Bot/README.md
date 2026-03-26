# Context Handling for Follow-up Queries

## Description
This chatbot supports short multi-turn conversations by maintaining minimal conversation state.

It remembers:
- Last detected intent
- Extracted semester

## Example
User: When is the exam?
Bot: For which semester?
User: Semester 5
Bot: Semester 5 exams start on March 20.

## Concepts Used
- Basic intent detection
- Regex-based entity extraction
- Conversation state management

## workflow diagram 
```mermaid
flowchart TD
    A[User Query] --> B[Preprocessing]
    B --> C[Check Conversation History]
    C --> D[Combine Context + Query]
    D --> E[Intent Detection]
    E --> F[Retrieve Answer]
    F --> G[Generate Response]
    G --> H[Update Memory]
    H --> I[Output to User]