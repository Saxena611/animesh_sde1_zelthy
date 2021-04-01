"""
This program calls the main dictionary_search_main which internally calls dictionary api
for fetching the word meaning.
dictionary_search_main comprises of the DicitonarySearch class and provides all the required
methods in order to achieve the desired result.
"""
from assignment_2 import dictionary_search_main as dsm

## initializing object ##
word = str(input("Word ? "))
obj = dsm.DictionarySearch() # calling class constructor
output = obj.search_word(word) # calling class method to make an api call
print(output) # prinitng the response
#########################



