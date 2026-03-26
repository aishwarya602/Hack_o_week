# Entity Extraction for Student Queries

## Description
A rule-based entity extraction system that identifies:
- Semester numbers
- Course codes
- Dates

from student queries using regular expressions.

## Technologies Used
- Python
- Regular Expressions (re module)

## Example
Input: When is sem 5 CS101 exam on 12 March?
Output:
Semester: 5
Course: CS101
Date: 12 March

## workflow diagram
```mermaid
flowchart TD
    A[User Query] --> B[Preprocessing]
    B --> C[Tokenization]
    C --> D[Apply Rules / Regex / Keyword Matching]
    D --> E[Extract Entities]
    E --> F[Structure Data (JSON Format)]
    F --> G[Use in Database / Response System]
    G --> H[Output to User]