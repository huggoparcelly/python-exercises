def count_vowels(word):             # linha 1
    count = 0                       # linha 2 com um BREAKPOINT!
    for letter in word:             # linha 3
        count += is_vowel(letter)   # linha 4
    return count                    # linha 5


def is_vowel(letter):               # linha 8
    vowels = 'aeiou'                # linha 9 com um BREAKPOINT!
    return letter in vowels         # linha 10


print(count_vowels('BANANA'))      # linha 13