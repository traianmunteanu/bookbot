import sys as sys
from stats import count_words, count_characters, sort_char_counts

def get_book_text(book_path):
  with open(book_path) as f:
    return f.read()

def main():
  print("Usage: python3 main.py <path_to_book>")
  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  word_count = count_words(book_text)

  char_counts = count_characters(book_text)
  sorted_chars = sort_char_counts(char_counts)

  # Print the report in the exact format specified
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  # Print character counts for alphabetical characters only
  for char_dict in sorted_chars:
    char = char_dict["char"]
    count = char_dict["num"]
    # Only print alphabetical characters
    if char.isalpha():
      print(f"{char}: {count}")

  print("============= END ===============")

main()