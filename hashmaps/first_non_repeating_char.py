'''
Write an algorithm that returns the first non-repeated character in a string. For example:

Examples
1. 'ACBA' -> B
2. 'BCABAC' -> None
3. 'BAC' -> B
4. 'GlovoOnGlovo' -> O
5. 'What is the first non-repeated character?' -> W
'''


def get_first_non_repeated_character(s):
    '''Time O(n), Space O(1) - You only have a limited no of characters'''

    if not s:
        return None

    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in s:
        if freq[char] == 1:
            return char

    return None


assert get_first_non_repeated_character('') == None
assert get_first_non_repeated_character('ABCA') == 'B'
assert get_first_non_repeated_character('BCABAC') == None
assert get_first_non_repeated_character('BAC') == 'B'
assert get_first_non_repeated_character('GlovoOnGlovo') == 'O'
char = 'What is the first non-repeated character?'
assert get_first_non_repeated_character(char) == 'W'
