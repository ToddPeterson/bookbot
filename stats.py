from operator import itemgetter


def count_words(text):
   """Return the number of words in a string"""
   return  len(text.split())


def count_chars(text):
   """Return a dictionary containing the number of times each character is included in the text"""
   char_count = {}
   for char in text.lower():
      if char in char_count:
         char_count[char] += 1
      else:
         char_count[char] = 1
   return char_count


def char_count_report(char_count):
   """Return a sorted list of char counts"""
   char_list = [{'char': key, 'num': value} for (key, value) in char_count.items()]
   char_list.sort(key=itemgetter('num'), reverse=True)
   return char_list
