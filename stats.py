def count_words(text):
  return len(text.split())

def count_characters(text):
  char_count = {}
  for char in text:
    lower_char = char.lower()
    if lower_char in char_count:
      char_count[lower_char] += 1
    else:
      char_count[lower_char] = 1
  return char_count

def sort_char_counts(char_counts):
  # Convert dictionary to list of dictionaries
  char_list = []
  for char, count in char_counts.items():
    char_list.append({"char": char, "num": count})

  # Sort by count from greatest to least
  char_list.sort(key=lambda x: x["num"], reverse=True)
  return char_list
