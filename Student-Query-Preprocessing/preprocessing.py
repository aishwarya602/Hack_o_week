import string

# List of common stopwords
stopwords = {
    "is", "am", "are", "the", "a", "an", "in", "on", "at",
    "for", "to", "of", "and", "or", "with", "this", "that",
    "i", "you", "he", "she", "it", "we", "they"
}

# Basic spelling normalization dictionary
spelling_corrections = {
    "admisson": "admission",
    "feesess": "fees",
    "colleg": "college",
    "intitute": "institute",
    "timng": "timing"
}

def preprocess(text):
    print("Original Text:", text)

    # Lowercasing
    text = text.lower()
    print("\nAfter Lowercasing:", text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    print("\nAfter Removing Punctuation:", text)

    # Tokenization
    tokens = text.split()
    print("\nAfter Tokenization:", tokens)

    # Spelling Normalization
    normalized_tokens = []
    for word in tokens:
        if word in spelling_corrections:
            normalized_tokens.append(spelling_corrections[word])
        else:
            normalized_tokens.append(word)
    print("\nAfter Spelling Normalization:", normalized_tokens)

    # Stopword Removal
    filtered_tokens = [word for word in normalized_tokens if word not in stopwords]
    print("\nAfter Stopword Removal:", filtered_tokens)

    return filtered_tokens



user_input = input("Enter a student query: ")
final_output = preprocess(user_input)

print("\nFinal Preprocessed Output:", final_output)
