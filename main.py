import sys

from stats import (
   count_words,
   count_chars,
   char_count_report,
)


def get_book_text(filepath):
   """Read and return the contents of a file"""
   with open(filepath) as f:
      contents = f.read()
   return contents


def main(filepath):
   text = get_book_text(filepath)

   num_words = count_words(text)
   char_count = count_chars(text)
   char_report = char_count_report(char_count)

   print('============ BOOKBOT ============')
   print(f'Analyzing book found at {filepath}...')
   print('----------- Word Count ----------')
   print(f'Found {num_words} total words')
   print('--------- Character Count -------')
   for item in char_report:
      if item['char'].isalpha():
         print(f'{item["char"]}: {item["num"]}')
   print('============= END ===============')


if __name__ == '__main__':
   if len(sys.argv) < 2:
      print('Usage: python3 main.py <path_to_book>')
      sys.exit(1)

   filepath = sys.argv[1]
   main(filepath)
