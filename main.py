def main():
  frankenstein = "books/frankenstein.txt"
  book = open_book(frankenstein)
  words = count_words(book)
  letters_dict = count_letters(book)
  report(frankenstein, words, letters_dict)


def open_book(book_location):
  with open(book_location) as f:
    return f.read()

def count_words(book):
  words = book.split()
  return len(words)

def count_letters(book):
  lower_text = book.lower()
  letters = list(lower_text)
  letters_dict = {}
  for l in letters:
    if l in letters_dict:
      letters_dict[l] += 1
    else:
      letters_dict[l] = 1
  return letters_dict

def report(book, words, letters_dict):
  print(f"--- Begin report of {book} ---")
  print(f"{words} words found in the document\n")

  def sort_on(dict):
    return dict[1]

  my_list = list(letters_dict.items())
  my_list.sort(reverse=True, key=sort_on)
  for l in my_list:
    if l[0].isalpha():
      k = l[0]
      count = l[1]
      print(f"The '{k}' character was found {count} times")

  print("--- End report ---")



main()