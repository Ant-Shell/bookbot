from collections import Counter

def get_num_words(body):
  num_words = len(body.split())
  message = f"Found {num_words} total words"
  return message, get_string_occurrences(body)

def get_string_occurrences(body):
  lowercase_body = body.lower()
  string_occurrences = Counter(lowercase_body)
  return dict(string_occurrences)

def sort_on(dict):
  return dict["num"]

def get_sorted_list_of_dict(occurrences):
  list = []
  result = ""

  for key in occurrences:
    if key.isalpha():
      list.append({"name": key, "num": occurrences[key]})

  list.sort(reverse=True, key=sort_on)

  for dict in range(len(list)):
    result += f"{list[dict]["name"]}: {list[dict]["num"]}\n"

  return result
  