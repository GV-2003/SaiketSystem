import string
from collections import Counter

def analyze_text_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        # Count characters
        char_count = len(text)

        # Count lines
        line_count = text.count("\n") + 1 if text else 0

        # Clean text: lowercase and remove punctuation
        translator = str.maketrans("", "", string.punctuation)
        cleaned_text = text.lower().translate(translator)

        # Split into words
        words = cleaned_text.split()
        word_count = len(words)

        # Word frequency analysis
        word_freq = Counter(words)
        most_common_words = word_freq.most_common(10)

        # Display results
        print("\n TEXT FILE ANALYSIS RESULTS")
        print("-" * 40)
        print(f"Lines        : {line_count}")
        print(f"Words        : {word_count}")
        print(f"Characters   : {char_count}")

        print("\n🔤 Most Common Words:")
        for word, count in most_common_words:
            print(f"{word:<15} {count}")

    except FileNotFoundError:
        print(" File not found. Please check the filename.")


# Example usage
filename = "sample.txt"  # Replace with your file name
analyze_text_file(filename)
