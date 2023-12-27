# Function to count lines, words, and characters in a text file
def count_file_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_characters = sum(len(line) for line in lines)
            return num_lines, num_words, num_characters
    except FileNotFoundError:
        return 0, 0, 0
# Specify the path to your text file
file_path = 'note.txt'
# Call the function to count lines, words, and characters
num_lines, num_words, num_characters = count_file_info(file_path)
# Print the results
print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")
print(f"Number of characters: {num_characters}")
