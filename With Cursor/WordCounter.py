# Program to count words in a text file

# 1. Ask for the path to a text file
file_path = input("Enter the path to the text file: ")
file_path = file_path.strip().strip('"').strip("'")
import os
file_path = os.path.expandvars(os.path.expanduser(file_path))

# 2. Read the content of the file safely (handle missing file and encoding)
try:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found. Please check the path and try again.")
    import sys
    sys.exit(1)
except OSError as e:
    print(f"Error opening file: {e}")
    import sys
    sys.exit(1)


# 3. Separate into words (normalize case and strip punctuation)
import re
words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9']+", content.lower())

# 4. Count the total number of words
total_words = len(words)
print(f"Total words: {total_words}")

# 5. Display the 10 most frequent words and their count
from collections import Counter
counter = Counter(words)

for word, count in counter.most_common(10):
    print(f"{word}: {count}")
