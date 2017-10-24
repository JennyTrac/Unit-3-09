# Created by Jenny Trac
# Created on Oct 23 2017
# Program prints unicode alphabet

# constants and variables
LETTER_A = 0101
uppercase_counter = LETTER_A
LETTER_a = 0141
lowercase_counter = LETTER_a

# capital letters
print("Capital letters:")
for uppercase_counter in range(LETTER_A, LETTER_A + 26):
    uppercase_letter = unichr(uppercase_counter)
    print(uppercase_letter)
    
# lowercase letters
print("Lowercase letters:")
for lowercase_counter in range(LETTER_a, LETTER_a + 26):
    lowercase_letter = unichr(lowercase_counter)
    print(lowercase_letter)
