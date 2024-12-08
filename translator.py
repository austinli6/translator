# Basic English to French Translator
def english_to_french(word):
    # Dictionary with English to French translations
    dictionary = {
        "hello": "bonjour",
        "goodbye": "au revoir",
        "please": "s'il vous plaît",
        "thank you": "merci",
        "yes": "oui",
        "no": "non",
        "friend": "ami",
        "love": "amour",
        "food": "nourriture",
        "water": "eau"
    }

    # Lookup the word in the dictionary
    return dictionary.get(word.lower(), "Translation not found")


def main():
    print("Welcome to the Basic English to French Translator!")
    print("Type 'exit' to quit.\n")

    while True:
        # Get input from the user
        english_word = input("Enter an English word to translate: ").strip()
        
        # Exit condition
        if english_word.lower() == "exit":
            print("Goodbye! Merci!")
            break
        
        # Translate and display the result
        french_translation = english_to_french(english_word)
        print(f"The French translation of '{english_word}' is: {french_translation}\n")


if __name__ == "__main__":
    main()
