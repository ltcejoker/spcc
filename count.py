import re

# Function to count characters, words, sentences, lines, tabs, numbers, and blank spaces
def count_input(text):
    num_chars = 0
    num_words = 0
    num_sentences = 0
    num_lines = 0
    num_tabs = 0
    num_numbers = 0
    num_spaces = 0
    
    # Split text into lines
    lines = text.splitlines()
    num_lines = len(lines)
    
    for line in lines:
        num_chars += len(line)  # Count characters in the line
        num_tabs += line.count("\t")  # Count tabs in the line
        num_spaces += line.count(" ")  # Count blank spaces in the line
        
        # Count words
        words = re.findall(r'\b[a-zA-Z]+\b', line)  # Only count alphabetic words
        num_words += len(words)
        
        # Count numbers
        numbers = re.findall(r'\b\d+\b', line)
        num_numbers += len(numbers)
        
        # Count sentences (by recognizing punctuation marks: .?!)
        num_sentences += len(re.findall(r'[.!?]', line))

    return num_chars, num_words, num_sentences, num_lines, num_tabs, num_numbers, num_spaces

# Input text from the user
text = input("Enter the text: ")

# Call the function and get the counts
num_chars, num_words, num_sentences, num_lines, num_tabs, num_numbers, num_spaces = count_input(text)

# Display the results
print(f"Characters: {num_chars}")
print(f"Words: {num_words}")
print(f"Sentences: {num_sentences}")
print(f"Lines: {num_lines}")
print(f"Tabs: {num_tabs}")
print(f"Numbers: {num_numbers}")
print(f"Blank spaces: {num_spaces}")
