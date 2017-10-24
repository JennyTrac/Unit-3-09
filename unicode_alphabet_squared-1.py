# Created by Jenny Trac
# Created on Oct 24 2017
# Prints all possibilities for letter pairings of the alphabet

# constants and variables
LETTER_A = 0101
uppercase_counter = LETTER_A
LETTER_a = 0141
lowercase_counter = LETTER_a

for uppercase_counter in range(LETTER_A, LETTER_A + 26):
    for lowercase_counter in range(LETTER_a, LETTER_a + 26):
        letter_combination = unichr(uppercase_counter) + unichr(lowercase_counter)
        print(letter_combination)
    print(" ")
