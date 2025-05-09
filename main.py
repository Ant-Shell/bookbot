from stats import get_num_words, get_sorted_list_of_dict

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return get_num_words(file_contents)

def main():
  path_to_file = "books/frankenstein.txt"
  word_count_message, ocurrences = get_book_text(path_to_file)

  reformatted_ocurrences = get_sorted_list_of_dict(ocurrences)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path_to_file}")
  print("----------- Word Count ----------")
  print(f"{word_count_message}")
  print("--------- Character Count -------")
  print(f"{reformatted_ocurrences.rstrip()}")
  print("============= END ===============")

main()
